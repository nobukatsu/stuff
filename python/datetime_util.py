from datetime import datetime
import os


def get_datetime_from_date_suffix(file_name):

    root, ext = os.path.splitext(os.path.basename(file_name))
    if has_yymmdd_suffix(root): # this check has to come first to avoid 170302 -> 1703/02/01
        return datetime.strptime(root[-6:], "%y%m%d")
    elif has_yyyymm_suffix(root):
        return datetime.strptime(root[-6:], "%Y%m")
    elif has_yyyymmdd_suffix(root):
        return datetime.strptime(root[-8:], "%Y%m%d")
    else:
        return False


def has_yyyymm_suffix(target_text):

    date_text = target_text.split("_")
    date_text = date_text[len(date_text) - 1]
    date_text2 = target_text.split("-")
    date_text2 = date_text2[len(date_text2) - 1]

    try:
        datetime.strptime(date_text, "%Y%m")
        return len(date_text) == 6
    except ValueError:
        try:
            datetime.strptime(date_text2, "%Y%m")
            return len(date_text2) == 6
        except ValueError:
            return False


def has_yymmdd_suffix(target_text):

    date_text = target_text.split("_")
    date_text = date_text[len(date_text) - 1]
    date_text2 = target_text.split("-")
    date_text2 = date_text2[len(date_text2) - 1]

    try:
        datetime.strptime(date_text, "%y%m%d")
        return len(date_text) == 6
    except ValueError:
        try:
            datetime.strptime(date_text2, "%y%m%d")
            return len(date_text2) == 6
        except ValueError:
            return False


def has_yyyymmdd_suffix(target_text):

    date_text = target_text.split("_")
    date_text = date_text[len(date_text) - 1]
    date_text2 = target_text.split("-")
    date_text2 = date_text2[len(date_text2) - 1]

    try:
        datetime.strptime(date_text, "%Y%m%d")
        return len(date_text) == 8
    except ValueError:
        try:
            datetime.strptime(date_text2, "%Y%m%d")
            return len(date_text2) == 8
        except ValueError:
            return False
