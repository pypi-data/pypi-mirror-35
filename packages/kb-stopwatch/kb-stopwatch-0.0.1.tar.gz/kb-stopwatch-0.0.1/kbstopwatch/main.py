"""Contains the main function."""

import argparse
import signal
import sys
import time
import threading
import keyboard
from .version import NAME, DESCRIPTION, VERSION

# Control keys
CONTROL_KEY = 'space'


def format_time(seconds):
    """Returns seconds as a formatted string.

    The format is "hours:minutes:seconds.millisecond". Branko Bajcetic
    (@bbajcetic) wrote this function. Thanks!

    Arg:
        A float containing a number of seconds.

    Returns:
        A formatted string containing the time represented by the number
        of seconds passed in.
    """
    hours = seconds // 3600
    minutes = (seconds - (hours*3600)) // 60
    seconds = seconds - (hours*3600) - (minutes*60)
    time_elapsed = "{:02.0f}:{:02.0f}:{:06.3f}".format(hours, minutes, seconds)
    return time_elapsed


def timer_thread(event, start_time):
    """Show a timer.

    Args:
        event: A threading.Event which should be set to finish the
            function.
        start_time: A float specifying the starting time.
    """
    while not event.isSet():
        print(format_time(time.time() - start_time), end='\r')


def exit_program(*_, **__):
    """Exits the program."""
    sys.exit(0)


def main():
    """The main function."""
    # Add CLI to display help or the version
    parser = argparse.ArgumentParser(
        prog=NAME,
        description="%(prog)s - " + DESCRIPTION,)
    parser.add_argument(
        '--version',
        action='version',
        version="%(prog)s " + VERSION)

    parser.parse_args()

    # Exit gracefully from keyboard interrupt
    signal.signal(signal.SIGINT, exit_program)

    while True:
        # Wait for control key
        keyboard.wait(CONTROL_KEY)

        # Time!
        start_time = time.time()

        stop_event = threading.Event()
        timer = threading.Thread(
            target=timer_thread,
            args=(stop_event, start_time)).start()

        # Stop time!
        keyboard.wait(CONTROL_KEY)
        stop_event.set()

        # Print final time
        print(format_time(time.time() - start_time))
