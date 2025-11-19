from datetime import datetime as dt
from datetime import timezone as tz
from plotext._correct import correct_class as correct
from plotext._methods.list import is_list_like


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
            ('timestamp', 'timestamp'): lambda x: x
        }
        self.clear()

    # Reset to default settings
    def clear(self):
        self.set_form()
        self.set_origin('01/01/1900')
        self._set_active(False)

    # Set string format for date parsing
    def set_form(self, form = None):
        form = '%d/%m/%Y' if form is None else form
        self._form = form
        return self

    # Set origin timestamp for calculations
    def set_origin(self, string):
        self._origin = self._string_to_datetime(string).timestamp()
        return self

    # Activate or deactivate converter
    def _set_active(self, active = False):
        self._active = active
        return self

    # Get origin in requested output type
    def get_origin(self, output = "datetime"):
        return self.convert(self._origin, output)

    # Get today's date in requested output type
    def get_today(self, output = "datetime"):
        return self.convert(dt.today(), output)

    # Internal conversions
    def _string_to_datetime(self, string):
        return dt.strptime(string, self._form).replace(tzinfo = tz.utc)

    def _string_to_timestamp(self, string):
        return self._datetime_to_timestamp(self._string_to_datetime(string))

    def _datetime_to_string(self, datetime):
        return datetime.strftime(self._form)

    def _datetime_to_timestamp(self, datetime):
        return datetime.timestamp() - self._origin

    def _timestamp_to_datetime(self, timestamp):
        return dt.fromtimestamp(timestamp + self._origin).replace(tzinfo = tz.utc)

    def _timestamp_to_string(self, timestamp):
        return self._datetime_to_string(self._timestamp_to_datetime(timestamp))

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

    # Internal conversion functions
    def _convert(self, time, output = "datetime"):
        input = self._get_type(time)
        func = self._conversion_map[(input, output)]
        return func(time)

    def _convert_list(self, times, output = "datetime"):
        input = self._get_type(times[0])
        func = self._conversion_map[(input, output)]
        return [func(el) for el in times]

    # Public conversion function
    def convert(self, time, output = "timestamp"):
        return self._convert_list(time, output) if is_list_like(time) else self._convert(time, output)

    # Clone another date_class
    def _clone(self, date):
        self.set_form(form = date._form)
        self._active = date._active
        return self

    # Log string for representation
    def _get_log(self):
        return f", {'active' if self._active else 'inactive'}, form {repr(self._form)}, origin {self.get_origin('string')}"

    # Representation
    def __repr__(self):
        return f"DateConverter" + self._get_log()
