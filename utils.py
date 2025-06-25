from pytz import timezone, utc

def convert_utc_to_ist(dt):
    ist = timezone("Asia/Kolkata")
    return dt.astimezone(ist)
