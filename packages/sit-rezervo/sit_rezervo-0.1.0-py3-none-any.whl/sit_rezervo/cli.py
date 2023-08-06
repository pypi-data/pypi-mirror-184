import time
from datetime import datetime
from typing import Optional

import typer
import uvicorn
from pytz import timezone

from . import api
from .auth import AuthenticationError
from .booking import find_class
from .config import config_from_stream
from .cron_generator import generate_booking_cron_job
from .errors import BookingError
from .main import try_book_class, try_authenticate
from .notify.notify import notify_booking_failure, notify_auth_failure
from .utils.time_utils import readable_seconds
from .api import api as api_app, get_configs

cli = typer.Typer()


@cli.command()
def book(
        class_id: int,
        check_run: bool = typer.Option(False, "--check", help="Perform a dry-run to verify that booking is possible"),
        config_stream: typer.FileText = typer.Option(
            "config.yaml",
            "--config-file", "-c",
            encoding="utf-8",
            help="Configurations file"
        ),
) -> None:
    """
    Book the class with config index matching the given class id
    """
    print("[INFO] Loading config...")
    config = config_from_stream(config_stream)
    if config is None:
        print("[ERROR] Failed to load config, aborted.")
        return
    if not 0 <= class_id < len(config.classes):
        print(f"[ERROR] Class index out of bounds")
        return
    _class_config = config.classes[class_id]
    if config.booking.max_attempts < 1:
        print(f"[ERROR] Max booking attempts should be a positive number")
        if config.notifications is not None:
            notify_booking_failure(config.notifications, _class_config, BookingError.INVALID_CONFIG, check_run)
        return
    print("[INFO] Authenticating...")
    auth_result = try_authenticate(config.auth.email, config.auth.password, config.auth.max_attempts)
    if isinstance(auth_result, AuthenticationError):
        print("[ERROR] Abort!")
        if config.notifications is not None:
            notify_auth_failure(config.notifications, auth_result, check_run)
        return
    class_search_result = find_class(auth_result, _class_config)
    if isinstance(class_search_result, BookingError):
        print("[ERROR] Abort!")
        if config.notifications is not None:
            notify_booking_failure(config.notifications, _class_config, class_search_result, check_run)
        return
    if check_run:
        print("[INFO] Check complete, all seems fine.")
        raise typer.Exit()
    _class = class_search_result
    if _class['bookable']:
        print("[INFO] Booking is already open, booking now!")
    else:
        # Retrieve booking opening, and make sure it's timezone aware
        tz = timezone(config.booking.timezone)
        opening_time = tz.localize(datetime.fromisoformat(_class['bookingOpensAt']))
        timedelta = opening_time - datetime.now(tz)
        wait_time = timedelta.total_seconds()
        wait_time_string = readable_seconds(wait_time)
        if wait_time > config.booking.max_waiting_minutes * 60:
            print(f"[ERROR] Booking waiting time was {wait_time_string}, "
                  f"but max is {config.booking.max_waiting_minutes} minutes. Aborting.")
            if config.notifications is not None:
                notify_booking_failure(config.notifications, _class_config, BookingError.TOO_LONG_WAITING_TIME)
            raise typer.Exit(1)
        print(f"[INFO] Scheduling booking at {datetime.now(tz) + timedelta} "
              f"(about {wait_time_string} from now)")
        time.sleep(wait_time)
        print(f"[INFO] Awoke at {datetime.now(tz)}")
    booking_result = try_book_class(auth_result, _class, config.booking.max_attempts, config.notifications)
    if isinstance(booking_result, BookingError):
        if config.notifications is not None:
            notify_booking_failure(config.notifications, _class_config, booking_result, check_run)
        raise typer.Exit(1)


@cli.command()
def cron(
        config_streams: list[typer.FileText] = typer.Option(
            ["config.yaml"],
            "--config-file", "-c",
            encoding="utf-8",
            help="Configurations file (multiple allowed)"
        ),
        output_file: Optional[typer.FileTextWrite] = typer.Option(None, "--output-file", "-o", encoding="utf-8"),
):
    """
    Generate cron jobs for class booking
    """
    cron_spec = ""
    for config_stream in config_streams:
        config = config_from_stream(config_stream)
        for i, c in enumerate(config.classes):
            cron_spec += generate_booking_cron_job(i, c, config.cron, config_stream.name)
    if output_file is not None:
        output_file.write(cron_spec + "\n")
        raise typer.Exit()
    print(cron_spec)


@cli.command(
    name="api",
    context_settings={"allow_extra_args": True, "ignore_unknown_options": True}  # Enabled to support uvicorn options
)
def serve_api(
        ctx: typer.Context,
        config_streams: list[typer.FileText] = typer.Option(
            ["config.yaml"],
            "--config-file", "-c",
            encoding="utf-8",
            help="Configurations file (multiple allowed)"
        ),
):
    """
    Start a web server to handle Slack message interactions

    Actually a wrapper around uvicorn, and supports passing additional options to the underlying uvicorn.run() command.
    """
    ctx.args.insert(0, f"{api.__name__}:api")
    configs = [config_from_stream(cs) for cs in config_streams]
    api_app.dependency_overrides[get_configs] = lambda: configs
    uvicorn.main.main(args=ctx.args)


@cli.callback()
def callback():
    """
    Automatic booking of Sit Trening group classes
    """
