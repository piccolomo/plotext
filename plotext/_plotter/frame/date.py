# Date: converts between string, datetime and timestamp representations with a configurable origin

from datetime import datetime as dt
from datetime import timezone as tz
from datetime import timedelta
from plotext._methods.object import is_list_like
from plotext._settings.defaults import date_origin_datetime


# The moment every timestamp is counted from, used to turn one back into a date by hand
epoch_datetime = dt(1970, 1, 1, tzinfo = tz.utc)


# Date converter: handles string / datetime / timestamp conversions
class date_class:

    # Initialize the date converter
    def __init__(self):
        self._conversion_map = {
            ('string', 'string'): lambda x, relative = True: x,
            ('string', 'datetime'): self._string_to_datetime,
            ('string', 'timestamp'): self._string_to_timestamp,
            ('datetime', 'string'): self._datetime_to_string,
            ('datetime', 'datetime'): lambda x, relative = True: x,
            ('datetime', 'timestamp'): self._datetime_to_timestamp,
            ('timestamp', 'string'): self._timestamp_to_string,
            ('timestamp', 'datetime'): self._timestamp_to_datetime,
            ('timestamp', 'timestamp'): lambda x, relative = True: x}
        self.clear()

    # Reset to default settings
    def clear(self):
        self._set_form()
        self._set_zone()
        self._origin = date_origin_datetime.timestamp()
        self._set_active(False)

    # Set string format for date parsing
    def _set_form(self, form = None):
        form = '%d/%m/%Y' if form is None else form
        self._form = form
        return self

    # Set the zone the axis is written in, given as the hours from UTC, 0 by default and 5.5 for India
    def _set_zone(self, zone = None):
        self._zone_hours = 0 if zone is None else zone
        return self

    # The zone as an object the datetime package understands
    def _get_zone(self):
        return tz(timedelta(hours = self._zone_hours))

    # Set origin timestamp for calculations
    def _set_origin(self, origin = None):
        origin = date_origin_datetime if origin is None else origin
        if self._get_type(origin) is None:
            raise ValueError(f"origin {origin!r} does not match the current form {self._form!r} and is not a recognised datetime / timestamp. Set the form first (or pass a matching string).")
        self._origin = self._convert_time(origin, "timestamp", relative = False)
        return self

    # Activate or deactivate converter
    def _set_active(self, active = False):
        self._active = active
        return self

    # Activate (or deactivate) date handling on this ruler with optional form, origin and zone in one call
    def activate(self, active = True, form = None, origin = None, zone = None):
        self._set_active(active)
        self._set_form(form) if form is not None else None
        self._set_zone(zone) if zone is not None else None
        self._set_origin(origin) if origin is not None else None
        return self

    # Get origin in requested output type
    def origin(self, output = "datetime"):
        return self._convert_time(self._origin, output, relative = False)

    # Today in the requested form (string / datetime / timestamp)
    def today(self, output = "datetime"):
        return self._convert_time(dt.today(), output)

    # Check if converter is active
    def active(self):
        return self._active

    # Convert a string to a datetime, read in the zone of the axis (relative is a dummy parameter kept for signature uniformity)
    def _string_to_datetime(self, string, relative = True):
        return dt.strptime(string, self._form).replace(tzinfo = self._get_zone())

    # Convert a string to a timestamp, routing through datetime
    def _string_to_timestamp(self, string, relative = True):
        return self._datetime_to_timestamp(self._string_to_datetime(string), relative = relative)

    # Convert a datetime to a string (relative is a dummy parameter)
    def _datetime_to_string(self, datetime, relative = True):
        return datetime.strftime(self._form)

    # Convert a datetime to a timestamp, subtracting the origin when requested; a datetime carrying no zone is read in the zone of the axis, as a date written as text is, and one carrying its own keeps it
    def _datetime_to_timestamp(self, datetime, relative = True):
        datetime = datetime if datetime.tzinfo is not None else datetime.replace(tzinfo = self._get_zone())
        return datetime.timestamp() - self._origin * relative

    # Convert a timestamp to a datetime in the zone of the axis, adding the origin when requested; the seconds are counted from the 1st of January 1970 by hand, since Windows refuses to convert a moment before it
    def _timestamp_to_datetime(self, timestamp, relative = True):
        return (epoch_datetime + timedelta(seconds = timestamp + self._origin * relative)).astimezone(self._get_zone())

    # Convert a timestamp to a string, routing through datetime
    def _timestamp_to_string(self, timestamp, relative = True):
        return self._datetime_to_string(self._timestamp_to_datetime(timestamp, relative = relative), relative = relative)

    # Determine type of input
    def _get_type(self, time):
        return "string" if self._is_string_date(time) else "datetime" if isinstance(time, dt) else "timestamp" if isinstance(time, (int, float)) else None

    # Check if string can be converted to date
    def _is_string_date(self, time):
        try:
            self._string_to_datetime(time)
            return True
        except:
            return False

    # Internal conversion for a single value
    def _convert_time(self, time, output = "datetime", relative = True):
        input = self._get_type(time)
        func = self._conversion_map[(input, output)]
        return func(time, relative = relative)

    # Internal conversion for a list of values
    def _convert_list(self, times, output = "datetime"):
        if len(times) == 0: return []
        input = self._get_type(times[0])
        func = self._conversion_map[(input, output)]
        return [func(el) for el in times]

    # Public conversion function
    def convert(self, time, output = "timestamp"):
        return self._convert_list(time, output) if is_list_like(time) else self._convert_time(time, output)

    # Clone another date_class
    def _clone(self, date):
        self._set_form(form = date._form)
        self._set_zone(zone = date._zone_hours)
        self._origin = date._origin
        self._active = date._active
        return self

    # Log string for representation
    def _get_log(self):
        base = f"{'active' if self._active else 'inactive'}, form {repr(self._form)}"
        return f"{base}, zone {self._zone_hours}, origin {self.origin('string')}" if self._active else base

    # Representation
    def __repr__(self):
        return "PlotextDate(" + self._get_log() + ")"
