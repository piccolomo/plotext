# Date: converts between string, datetime and timestamp representations with a configurable origin

from datetime import datetime as dt
from datetime import timezone as tz
from plotext._methods.object import is_list_like
from plotext._settings.defaults import date_origin_string


# Date converter: handles string / datetime / timestamp conversions
class date_class:

    # Initialize the date converter
    def __init__(self):
        self._conversion_map = {
            ('string', 'string'): lambda x: x,
            ('string', 'datetime'): self._string_to_datetime,
            ('string', 'timestamp'): self._string_to_timestamp,
            ('datetime', 'string'): self._datetime_to_string,
            ('datetime', 'datetime'): lambda x: x,
            ('datetime', 'timestamp'): self._datetime_to_timestamp,
            ('timestamp', 'string'): self._timestamp_to_string,
            ('timestamp', 'datetime'): self._timestamp_to_datetime,
            ('timestamp', 'timestamp'): lambda x: x}
        self.clear()

    # Reset to default settings
    def clear(self):
        self.set_form()
        self._origin = 0
        self._set_active(False)

    # Set string format for date parsing
    def set_form(self, form = None):
        form = '%d/%m/%Y' if form is None else form
        self._form = form
        return self

    # Set origin timestamp for calculations
    def set_origin(self, origin = None):
        origin = date_origin_string if origin is None else origin
        self._origin = self._convert_time(origin, "timestamp", consider_origin = False)
        return self

    # Activate or deactivate converter
    def _set_active(self, active = False):
        self._active = active
        return self

    # Get origin in requested output type
    def get_origin(self, output = "datetime"):
        return self._convert_time(self._origin, output, consider_origin = False)

    # Get today's date in requested output type
    def get_today(self, output = "datetime"):
        return self._convert_time(dt.today(), output)

    # Check if converter is active
    def is_active(self):
        return self._active

    # Convert a string to a datetime (consider_origin is a dummy parameter kept for signature uniformity)
    def _string_to_datetime(self, string, consider_origin = True):
        return dt.strptime(string, self._form).replace(tzinfo = tz.utc)

    # Convert a string to a timestamp, routing through datetime
    def _string_to_timestamp(self, string, consider_origin = True):
        return self._datetime_to_timestamp(self._string_to_datetime(string), consider_origin = consider_origin)

    # Convert a datetime to a string (consider_origin is a dummy parameter)
    def _datetime_to_string(self, datetime, consider_origin = True):
        return datetime.strftime(self._form)

    # Convert a datetime to a timestamp, subtracting the origin when requested
    def _datetime_to_timestamp(self, datetime, consider_origin = True):
        return datetime.timestamp() - self._origin * consider_origin

    # Convert a timestamp to a datetime, adding the origin when requested
    def _timestamp_to_datetime(self, timestamp, consider_origin = True):
        return dt.fromtimestamp(timestamp + self._origin * consider_origin).replace(tzinfo = tz.utc)

    # Convert a timestamp to a string, routing through datetime
    def _timestamp_to_string(self, timestamp, consider_origin = True):
        return self._datetime_to_string(self._timestamp_to_datetime(timestamp, consider_origin = consider_origin), consider_origin = consider_origin)

    # Determine type of input
    def _get_type(self, time):
        return "string" if self._is_string_date(time) else "datetime" if isinstance(time, dt) else "timestamp" if isinstance(time, float) else None

    # Check if string can be converted to date
    def _is_string_date(self, time):
        try:
            self._string_to_datetime(time)
            return True
        except:
            return False

    # Internal conversion for a single value
    def _convert_time(self, time, output = "datetime", consider_origin = True):
        input = self._get_type(time)
        func = self._conversion_map[(input, output)]
        return func(time, consider_origin = consider_origin)

    # Internal conversion for a list of values
    def _convert_list(self, times, output = "datetime"):
        input = self._get_type(times[0])
        func = self._conversion_map[(input, output)]
        return [func(el) for el in times]

    # Public conversion function
    def convert(self, time, output = "timestamp"):
        return self._convert_list(time, output) if is_list_like(time) else self._convert_time(time, output)

    # Clone another date_class
    def clone(self, date):
        self.set_form(form = date._form)
        self._active = date._active
        return self

    # Log string for representation
    def get_log(self):
        return f"{'active' if self._active else 'inactive'}, form {repr(self._form)}, origin {self.get_origin('string')}"

    # Representation
    def __repr__(self):
        return f"Plotext Date: " + self.get_log()
