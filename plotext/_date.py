from datetime import datetime as dt
from datetime import timezone as tz # useful for dates before 1970 in windows

class date_class():
    
    def __init__(self):
        self.date_form()
        self.time0 = 0
        self.set_time0('01/01/1900')

    def date_form(self, input_form = None, output_form = None): # it sets the datetime form used for functions that output date string and input date string
        input_form = 'd/m/Y' if input_form is None else input_form
        output_form = input_form if output_form is None else output_form
        self.input_form = self.correct_form(input_form)
        self.output_form = self.correct_form(output_form)
        
    def set_time0(self, string, input_form = None): # the origin of time, useful for log scale not to hit the 0 timestamp
        self.time0 = self.string_to_time(string, input_form, 0)

    def today_datetime(self): # today in datetime form
        return dt.today()
    
    def today_string(self, output_form = None): # today in string form
        return self.datetime_to_string(self.today_datetime(), output_form)
    
    def datetime_to_string(self, datetime, output_form = None): # from datetime form to string form
        output_form = self.output_form if output_form is None else self.correct_form(output_form)
        return datetime.strftime(output_form)
    
    def datetimes_to_strings(self, datetimes, output_form = None): # from datetime form to string form
        return [self.datetime_to_string(el, output_form) for el in datetimes]

    def string_to_datetime(self, string, input_form = None): # from date and times in string form to standard datetime input_form
        input_form = self.input_form if input_form is None else self.correct_form(input_form)
        return dt.strptime(string, input_form)

##############################################
############     Utilities    ################
##############################################

    def correct_form(self, date_form):
        return ''.join(['%' + el if el.isalpha() else el for el in date_form])

    def string_to_time(self, string, input_form = None, time0 = None):
        input_form = self.input_form if input_form is None else self.correct_form(input_form)
        time0 = self.time0 if time0 is None else time0
        try:
            return dt.strptime(string, input_form).replace(tzinfo = tz.utc).timestamp() - time0
        except:
            raise ValueError('Date Form should be: ' + input_form)

    def strings_to_time(self, strings, input_form = None):
        return [self.string_to_time(el, input_form) for el in strings]

    def time_to_string(self, time, output_form = None):
        return self.datetime_to_string(dt.fromtimestamp(time + self.time0), output_form)
    
    def times_to_string(self, times, input_form = None):
        return [self.time_to_string(el, input_form) for el in times]

