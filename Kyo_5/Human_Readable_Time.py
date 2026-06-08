def make_readable(seconds):
    hours = seconds // 3600

    remaining_seconds = seconds % 3600

    minutes = remaining_seconds // 60

    seconds = remaining_seconds % 60

    answer = f"{hours:02d}:{minutes:02d}:{seconds:02d}"

    return answer


# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python