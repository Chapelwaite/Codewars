def was_package_received_yesterday(tz_from, tz_to, start, duration):
    arrival = start + duration - tz_from + tz_to
    return arrival < 0


# https://www.codewars.com/kata/6707688c0f597511f6649270/train/python