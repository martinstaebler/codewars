def format_duration(seconds):
    # define duration of units
    one_year = 365 * 24 * 60 * 60
    one_day = 24 * 60 * 60
    one_hour = 60 * 60
    one_minute = 60

    # count units
    count_years = seconds // one_year
    count_days = seconds % one_year // one_day
    count_hours = seconds % one_day // one_hour
    count_minutes = seconds % one_hour // one_minute
    count_seconds = seconds % one_minute

    # define segments for output
    string_seconds =str(count_seconds) + " seconds" if count_seconds > 1 else str(count_seconds) + " second" if count_seconds == 1 else ""
    string_add_seconds = " and " if count_seconds > 0 and (count_minutes > 0 or count_hours > 0 or count_days > 0 or count_years > 0) else ""
    string_minutes = str(count_minutes) + " minutes" if count_minutes > 1 else str(count_minutes) + " minute" if count_minutes == 1 else ""
    string_add_minutes = " and " if (count_minutes > 0 and count_seconds == 0 and (count_hours > 0 or count_days > 0 or count_years > 0)) else ", " if (count_minutes > 0 and count_seconds > 0 and (count_hours > 0 or count_days > 0 or count_years > 0)) else ""
    string_hours = str(count_hours) + " hours" if count_hours > 1 else str(count_hours) + " hour" if count_hours == 1 else ""
    string_add_hours = " and " if (count_hours > 0 and (count_minutes == 0 and count_seconds == 0) and (count_days > 0 or count_years > 0)) else ", " if (count_hours > 0 and (count_seconds > 0 or count_minutes > 0) and (count_days > 0 or count_years > 0)) else ""
    string_days = str(count_days) + " days" if count_days > 1 else str(count_days) + " day" if count_days == 1 else ""
    string_add_days = " and " if (count_days > 0 and (count_hours == 0 and count_minutes == 0 and count_seconds == 0) and count_years > 0) else ", " if (count_days > 0 and (count_hours > 0 or count_seconds > 0 or count_minutes > 0) and count_years > 0) else ""
    string_years = str(count_years) + " years" if count_years > 1 else str(count_years) + " year" if count_years == 1 else ""

    # add segments to one string
    string_duration = string_years + string_add_days + string_days + string_add_hours + string_hours + string_add_minutes + string_minutes + string_add_seconds + string_seconds

    return string_duration if seconds > 0 else "now"


print(format_duration(60))    # returns "1 minute and 2 seconds"
print(format_duration(61))    # returns "1 minute and 2 seconds"
print(format_duration(62))    # returns "1 minute and 2 seconds"
print(format_duration(3662))  # returns "1 hour, 1 minute and 2 seconds"
print(format_duration(40213560))  # returns "1 hour, 1 minute and 2 seconds"

def format_duration_1(seconds):
    if seconds == 0: return "now"
    units = ( (31536000, "year"  ),
              (   86400, "day"   ),
              (    3600, "hour"  ),
              (      60, "minute"),
              (       1, "second") )
    ts, t = [], seconds
    for unit in units:
        u, t = divmod(t, unit[0])
        ts += ["{} {}{}".format(u, unit[1], "s" if u>1 else "")] if u != 0 else []
    return ", ".join([str(d)for d in ts[:-1]]) + (" and " if len(ts)>1 else "") + ts[-1]

def format_duration_2(s):
    dt = []
    for b, w in [(60, 'second'), (60, 'minute'), (24, 'hour'), (365, 'day'), (s+1, 'year')]:
        s, m = divmod(s, b)
        if m: dt.append('%d %s%s' % (m, w, 's' * (m > 1)))
    return ' and '.join(', '.join(dt[::-1]).rsplit(', ', 1)) or 'now'