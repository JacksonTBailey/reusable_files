import datetime
from dateutil.relativedelta import relativedelta



class DateHelper:
    def __init__(self):
        self.today = datetime.date.today()
        self.now = datetime.datetime.now()


    def get_current_month(self):
        """Returns the current month as a string in the format "MM".
        
        Returns:
            str: The current month as a string in the format "MM".
        """
        current_month = self.today.strftime("%#m")
        return current_month


    def get_current_full_date(self):
        """Returns the current date as a string in the format "MM-DD-YYYY".
        
        Returns:
            str: The current date as a string in the format "MM-DD-YYYY".
        """
        current_day = self.today.strftime("%#m-%#d-%Y")
        return current_day


    def get_current_time_of_day(self):
        """Returns the current time of day as a string in the format "AM" or "PM".
        
        Returns:
            str: The current time of day as a string in the format "AM" or "PM".
        """
        current_time = self.now.astimezone()
        am_or_pm = current_time.strftime("%p")
        return am_or_pm
    

    def add_time(self, **kwargs):
        """Returns the current date and time plus the specified amount of time.
        
        Args:
            **kwargs: The amount of time to add, in the format "days=X", "months=X", "years=X", "hours=X", "minutes=X", "seconds=X".
        
        Returns:
            datetime: The current date and time plus the specified amount of time.
        """
        current_datetime = self.now
        for key, value in kwargs.items():
            if key == "days":
                current_datetime += datetime.timedelta(days=value)
            elif key == "months":
                current_datetime += datetime.timedelta(days=30*value)
            elif key == "years":
                current_datetime += datetime.timedelta(days=365*value)
            elif key == "hours":
                current_datetime += datetime.timedelta(hours=value)
            elif key == "minutes":
                current_datetime += datetime.timedelta(minutes=value)
            elif key == "seconds":
                current_datetime += datetime.timedelta(seconds=value)
            else:
                raise ValueError(f"Invalid time parameter: {key}")
        return current_datetime


def subtract_time(self, **kwargs):
    """Returns the current date and time minus the specified amount of time.
    
    Args:
        **kwargs: The amount of time to subtract, in the format "days=X", "months=X", "years=X", "hours=X", "minutes=X", "seconds=X".
    
    Returns:
        datetime: The current date and time minus the specified amount of time.
    """
    current_datetime = datetime.datetime.now()
    for key, value in kwargs.items():
        if key == "days":
            current_datetime -= datetime.timedelta(days=value)
        elif key == "months":
            current_datetime -= relativedelta(months=value)
        elif key == "years":
            current_datetime -= relativedelta(years=value)
        elif key == "hours":
            current_datetime -= datetime.timedelta(hours=value)
        elif key == "minutes":
            current_datetime -= datetime.timedelta(minutes=value)
        elif key == "seconds":
            current_datetime -= datetime.timedelta(seconds=value)
        else:
            raise ValueError(f"Invalid time unit: {key}")
    return current_datetime