from .todo_utils import *


def get_pretty_time_string(delta_data):
    measure = {
        -1: "Less than minute ago",
        0: "day",
        1: "hour",
        2: "minute",
        10: "days",
        11: "hours",
        12: "minutes",
    }
    measure_value, data = get_first_not_zero_value(*delta_data)
    return (
        measure[-1] if measure_value == -1 else f"{data} {measure[measure_value]} ago"
    )


def substract_two_dates(date_given):
    diff = datetime.now() - datetime.fromisoformat(date_given)
    days = diff.days
    seconds = diff.seconds
    hours, remainder = divmod(seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return get_pretty_time_string([days, hours, minutes])


def get_human_readable_time(date_given):
    return substract_two_dates(date_given)
