from datetime import datetime as dt
from datetime import timezone as tz # useful for dates before 1970 in windows
from plotext._correct import correct_class as correct
from plotext._methods.list import is_list_like#, is_list_of_strings


class date_class():
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

    def clear(self):
        self.set_form()
        self.set_origin('01/01/1900') 
        self._set_active(False)

    def set_form(self, form = None): # it sets the datetime form used for functions that output date string and input date string
        form = '%d/%m/%Y' if form is None else form
        self._form = form 
        return self

    def set_origin(self, string): # the origin of time, useful for log scale not to hit the 0 timestamp
        self._origin = self._string_to_datetime(string).timestamp() 
        return self

    def _set_active(self, active = False):
        self._active = active
        return self 


    def get_origin(self, output = "datetime"):
        return self.convert(self._origin, output)

    def get_today(self, output = "datetime"): # today in datetime form
        return self.convert(dt.today(), output)



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


    def _get_type(self, time):
        return "string" if self._is_string_date(time) else "datetime" if isinstance(time, dt) else "timestamp" if isinstance(time, float) else None

    def _is_string_date(self, time):
        try: 
            self._string_to_datetime(time)
            return True
        except:
            return False

    # def _is_date(self, time):
    #     return self._get_type(time) in ["string", "datetime"]

    # def _are_dates(self, data, depth = 5):
    #     return is_list_like(data) and all([self._is_date(el) for el in data[ : depth]])


    def _convert(self, time, output = "datetime"):
        input = self._get_type(time)
        func = self._conversion_map[(input, output)]
        return func(time)

    def _convert_list(self, times, output = "datetime"):
        input = self._get_type(times[0])
        func = self._conversion_map[(input, output)]
        return [func(el) for el in times]


    def convert(self, time, output = "timestamp"):
        return self._convert_list(time, output) if is_list_like(time) else self._convert(time, output)



    def _clone(self, date):
        self.set_form(form = date._form)
        self._active = date._active
        return self

    def _get_log(self):
        return f", {"active" if self._active else "inactive"}, form {repr(self._form)}, origin {self.get_origin("string")}"

    def __repr__(self):
        return f"DateConverter" + self._get_log()

    # def get_today_string(self): # today in string form
    #     return self.datetime_to_string(self.today_datetime(), output_form)