import copy
import datetime
import pytz


def timezone_shanghai(row, field):
    row = copy.deepcopy(row)

    if isinstance(row[field], datetime.datetime):
        row[field] = row[field].replace(tzinfo=pytz.utc)
        row[field] = row[field].astimezone(pytz.timezone('Asia/Shanghai'))
    return row
