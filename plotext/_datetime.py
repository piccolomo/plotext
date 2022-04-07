from datetime import datetime as dt
from datetime import timezone as _tz # usefull for dates before 1970 in windows

def datetime_to_tuple(datetime): #  from datetime form to tuple form for dates
    day, month, year, hour, minute, second = datetime.day, datetime.month, datetime.year, datetime.hour, datetime.minute, datetime.second
    return (day, month, year, hour, minute, second)

class date_class():
    def __init__(self):
        self.input_date_form('d/m/Y H:M:S')
        self.output_date_form('d/m/Y H:M:S')

        self.time0 = 0
        self.set_time0('01/01/1900 00:00:00')

    def input_date_form(self, form):
        self.input_form = self.correct_form(form)
        
    def output_date_form(self, form):
        self.output_form = self.correct_form(form)
        
    def correct_form(self, date_form):
        return ''.join(['%' + el if el.isalpha() else el for el in date_form])

    def set_time0(self, string, form = None):
        self.time0 = self.string_to_time(string, form, 0)

    def string_to_time(self, string, form = None, time0 = None):
        form = self.input_form if form is None else self.correct_form(form)
        time0 = self.time0 if time0 is None else time0
        try:
            return dt.strptime(string, form).timestamp() - time0
        except:
            raise ValueError('Date Form should be: ' + form)

    def strings_to_time(self, strings):
        return [self.string_to_time(el) for el in strings]

    def datetime_to_string(self, datetime, form = None): # from datetime form to string form
        form = self.output_form if form is None else self.correct_form(form)
        return datetime.strftime(form)
    
    def datetimes_to_string(self, datetimes, form = None): # from datetime form to string form
        return [self.datetime_to_string(el, form) for el in datetimes]

    def string_to_datetime(self, string, form = None): # from date and times in string form to standard datetime form
        form = self.input_form if form is None else self.correct_form(form)
        return dt.strptime(string, form)

    def time_to_string(self, time, form = None):
        return self.datetime_to_string(dt.fromtimestamp(time + self.time0), form)
    
    def times_to_string(self, times, form = None):
        return [self.time_to_string(el, form) for el in times]

    def today_datetime(self):
        return dt.today()
    
    def today_string(self, form = None):
        return self.datetime_to_string(self.today_datetime(), form)

    def _strings_to_xlabels(self, strings): # this conversts a list of string dates into a list of reduced strings to be used for xlabels in the plot; where the previosu date is the same the next will omit the date and show only the time to reduce space 
        datetimes = [self.string_to_datetime(el) for el in strings]
        tuples = [datetime_to_tuple(el) for el in datetimes]
        labels = []
        for i in range(len(tuples)):
            if i > 0 and tuples[i][ : 3] == tuples[i - 1][ : 3]:
                s = self.datetime_to_string(datetimes[i], 0, 1)
            else:
                s = self.datetime_to_string(datetimes[i])
            labels.append(s)
        return labels 
