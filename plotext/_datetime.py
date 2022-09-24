from datetime import datetime as _dt
from datetime import timezone as _tz # usefull for dates before 1970 in windows

date_form = '%d/%m/%Y' # date string form
time_form = '%H:%M:%S' # time string form

def datetime_to_tuple(datetime): #  from datetime form to tuple form for dates
    day, month, year, hour, minute, second = datetime.day, datetime.month, datetime.year, datetime.hour, datetime.minute, datetime.second
    return (day, month, year, hour, minute, second)

def tuple_to_datetime(day = None, month = None, year = None, hour = 0, minute = 0, second = 0): # from tuple date form to datetime
    return _dt(year, month, day, hour, minute, second, tzinfo=_tz.utc)

class single_datetime_class():
    def __init__(self, datetime):
        self._set_datetime_form(date_form, time_form) 

        self.datetime = datetime
        self._to_tuple()

    def _set_datetime_form(self, date_form, time_form):
        self._date_form = date_form
        self._time_form = time_form
        self._datetime_form =  (date_form + ' ' + time_form).strip()

    def _to_tuple(self):
        self.tuple = datetime_to_tuple(self.datetime)
        return self.tuple

    def _to_timestamp(self):
        self._timestamp = self.datetime.timestamp()
        return self.timestamp

    def _to_string(self, date = True, time = True):
        self.string_date = self.datetime.strftime(self._date_form)
        self.string_time = self.datetime.strftime(self._time_form)
        self.string = self.datetime.strftime(self._datetime_form)
        return self.string
        
class datetime_class():
    def __init__(self):
        self.set_time0(1, 1, 1900) # day, month, year is the default origing of time which returns float timestamp = 0
        self.today = single_datetime_class(_dt.today()) # kind of useless for now
        self.set_datetime_form(date_form, time_form)
        self.today._to_string()

    def clear(self): # it clears mostly the date and time form
        self.__init__()

    def set_time0(self, day = None, month = None, year = None, hour = 0, minute = 0, second = 0): # it sets the origin of time, usefull when using log scale with dates to avoid hitting the 0 timestamp
        self._datetime0 = tuple_to_datetime(day, month, year, hour, minute, second)
        self._timestamp0 = self._datetime0.timestamp()

    def set_datetime_form(self, date_form = '', time_form = ''): # here you can decide the string form of dates and times
        self._date_form = date_form
        self._time_form = time_form
        self._datetime_form =  (date_form + ' ' + time_form).strip()
        self.today._set_datetime_form(date_form, time_form)

    def string_to_datetime(self, string, date = True, time = True): # from date and times in string form to standard datetime form
        if [date, time] == [True, False]:
            return _dt.strptime(string, self._date_form)
        elif [date, time] == [False, True]:
            return _dt.strptime(string, self._time_form)
        else:# [date, time] == [True, True]:
            return _dt.strptime(string, self._datetime_form)

    def datetime_to_timestamp(self, datetime): # from standard datetime to absolute float timestamp (relative to the origin of time set with time0)
        return datetime.timestamp() - self._timestamp0

    def string_to_timestamp(self, string): # from string form to float timestamp (relative to origin time0)
        return self.datetime_to_timestamp(self.string_to_datetime(string))

    def datetime_to_string(self, datetime, date = True, time = True): # from datetime form to string form
        string = ''
        if [date, time] == [True, False]:
            string = datetime.strftime(self._date_form)
        elif [date, time] == [False, True]:
            string = datetime.strftime(self._time_form)
        elif [date, time] == [True, True]:
            string = datetime.strftime(self._datetime_form)
        return string
    
        return datetime.strftime(self._datetime_form)
        string = string[:-9] if string[-8:] == '00:00:00' else string

    def _strings_to_xlabels(self, strings): # this conversts a list of string dates into a list of reduced strings to be used for xlabels in the plot; where the previosu date is the same the next will omit the date and show only the time to reduce space 
        datetimes = [self.string_to_datetime(el) for el in strings]
        tuples = [datetime_to_tuple(el) for el in datetimes]
        labels = []
        for i in range(len(tuples)):
            if i > 0 and tuples[i][ : 3] == tuples[i - 1][ : 3]:
                s = self.datetime_to_string(datetimes[i], 0, 1)
            else:
                s = self.datetime_to_string(datetimes[i], 1, 1)
            labels.append(s)
        return labels 
