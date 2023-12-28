from plotext._default import default_datetime_converter
from datetime import datetime as dt
from datetime import timezone as tz # usefull for dates before 1970 in windows
from pytz import timezone, all_timezones
from plotext._log import log


class date_class():
    def __init__(self):
        self.clear()

    def clear(self):
        self.date_form()
        self.all_timezones = all_timezones
        self.timezone()
        self.set_time0()

        
    def date_form(self, input_form = None, output_form = None): # it sets the datetime form used for functions that output date string and input date string
        self.input_form = default_datetime_converter.input_form if input_form is None else input_form
        self.output_form = default_datetime_converter.output_form if output_form is None else output_form
    
    def correct_input_form(self, input_form = None):
        return self.input_form if input_form is None else input_form

    def correct_output_form(self, output_form = None):
        return self.output_form if output_form is None else output_form

    
    def timezone(self, zone = None):
        self.zone = timezone(default_datetime_converter.zone)
        self.zone = self.correct_timezone(zone)

    def correct_timezone(self, zone = None):
        zone = self.zone.zone if zone is None else zone
        not_zone = zone.lower() not in [el.lower() for el in self.all_timezones]
        log.warning('Timezone not found; using default value (' + self.zone + ')') if not_zone else None
        zone = self.zone if not_zone else zone
        return timezone(zone)

    
    def set_time0(self, string = None, input_form = None): # the origin of time, usefull for log scale not to hit the 0 timestamp
        input_form = self.correct_input_form(input_form)
        string = default_datetime_converter.time0 if string is None else string
        self.time0 = self._string_to_datetime(string, input_form, self.zone)

        
    def _string_to_datetime(self, string, input_form, zone): # from date and times in string form to standard datetime input_form
        return dt.strptime(string, input_form).replace(tzinfo = zone)

    def strings_to_datetimes(self, strings, input_form = None, zone = None): # from date and times in string form to standard datetime input_form
        input_form = self.correct_input_form(input_form)
        zone = self.correct_timezone(zone)
        return [dt.strptime(string, input_form).replace(tzinfo = self.zone) for string in strings]

    
    def datetime_to_string(self, datetime, output_form = None): # from datetime form to string form
        output_form = self.correct_output_form(output_form)
        return datetime.strftime(output_form)
    
    def datetimes_to_strings(self, datetimes, output_form = None): # from datetime form to string form
        output_form = self.correct_output_form(output_form)
        return [el.strftime(output_form) for el in datetimes]

    
    def datetimes_to_numbers(self, datetimes):
        data = [time.timestamp() - self.time0.timestamp() for time in datetimes]
        return data
    convert = datetimes_to_numbers

    def numbers_to_strings(self, numbers):
        data = [el + self.time0.timestamp() for el in numbers]
        data = [dt.fromtimestamp(el) for el in data]
        data = self.datetimes_to_strings(data)
        return data

    def today(self): # today in datetime form
        return dt.today()
    
    def today_string(self, output_form = None): # today in string form
        return self.datetime_to_string(self.today(), output_form)
