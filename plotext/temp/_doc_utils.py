# this file contains all tools necessary to build the docstrings in _doc.py

from plotext._utility import pad_string, colorize, uncolorize
from inspect import getfullargspec as args
from re import sub
import copy



method_name_color = 'blue+'
method_name_style = 'bold'
alias_style = 'italic'

parameters_title_color = 'none'
parameters_title_style = 'none'

parameter_name_color = 'red+'
parameter_name_style = 'bold'

parameter_specs_color = 'orange+'
parameter_specs_style = 'dim'

parameter_doc_style = 'italic'

return_color = 'orange+'
return_style = 'bold'

warning = colorize('Warning', 'orange', 'bold')

nl = '\n'
sp = ' '
cm = ', '
sc = '; '

def correct_doc(doc):
   doc = doc.strip()
   doc = doc[:1].upper() + doc[1:]
   doc = doc if len(doc) == 0 or doc[-1] == '.' else doc + '.'
   doc = sub('  ', ' ', doc)
   return doc

class parameter_class(): # parameter doc
   def __init__(self, name, doc = '', type = '', default = ''):
      self.name = name.lower()
      self.doc = correct_doc(doc)
      self.type = None if type is None else str(type)
      self.set_default(default)

   def set_default(self, default = ''):
      if default == '':
         self.default = ''
      elif isinstance(default, str):
         self.default = "'" + default + "'"
      elif isinstance(default, float):
         self.default = str(round(default, 3))
      else:
         self.default = str(default)

   def get_doc(self):
      name = colorize(self.name, parameter_name_color, parameter_name_style)
      type = '' if self.type == '' else 'type: ' + str(self.type)
      default = '' if self.default == '' else  'default: ' + self.default
      specs = sc.join([spec for spec in [type, default] if spec != ''])
      specs = nl + colorize(specs, parameter_specs_color, parameter_specs_style) if specs != '' else ''
      doc = colorize(self.doc, style = parameter_doc_style)
      return nl + name + sp + doc + specs

   def copy(self, default = ''):
       par = copy.copy(self)
       par.set_default(default)
       return par

   
class parameters_class():
   def __init__(self):
      self.list = []

   def append(self, parameter):
      self.list.append(parameter)
   
   def add(self, name, doc = '', type = '', default = ''):
      self.append(parameter_class(name, doc, type, default))

   def get_title(self):
      lp = len(self.list)
      title = 'This is its parameter:' if lp == 1 else 'These are its parameters:'
      return colorize(title, parameters_title_color, parameters_title_style)

   def get_doc(self):
      docs = [el.get_doc() for el in self.list]
      return nl + self.get_title() + nl + nl.join(docs) if len(self.list) != 0 else ''

   def get_parameter(self, name):
      names = [el.name for el in self.list]
      if name not in names:
          print(warning, 'no parameter', name, 'found')
      index = names.index(name) if name in names else None
      return self.list[index] if name in names else None



class output_class():
   def __init__(self, doc = '', type = None):
      self.type = type
      self.doc = correct_doc(doc)

   def get_doc(self):
      title = colorize('Returns', return_color, return_style) 
      type = '' if self.type is None else 'type: ' + str(self.type)
      type = colorize(type , parameter_specs_color, parameter_specs_style) if type != '' else ''
      doc = colorize(self.doc, style = parameter_doc_style)
      return  nl + title + sp + doc + nl + type if self.doc != '' else ''

   
class method_class():
   def __init__(self, name, alias = None):
      self.name = name.lower()
      self.set_doc()
      self.alias = alias
      
      self.parameters = parameters_class()
      self.set_output()
      self.status = False
   
   def set_doc(self, doc = ''):
       self.doc = correct_doc(doc)

   def set_output(self, doc = '', type = ''):
      self.output = output_class(doc, type)

   def append_parameter(self, parameter_object):
      self.parameters.append(parameter_object)

   def add_parameter(self, name, doc = '', type = '', default = ''):
      self.parameters.add(name, doc, type, default)

   def get_title(self):
      return colorize(self.name, method_name_color, method_name_style)

   def get_doc(self):
      alias = (nl + "The methods " + colorize(self.name + '()', style = alias_style) + ' and ' + colorize(self.alias + '()', style = alias_style) + ' are equivalent.') if self.alias != '' else ''
      pars = self.parameters.get_doc()
      out = self.output.get_doc()
      return nl.join([el for el in [self.doc, alias, pars, out] if el != ''])

   def get_parameters(self):
      return [el.name for el in self.parameters.list]

   def get_parameter(self, name):
      return self.parameters.get_parameter(name)

   def show(self):
      print(self.get_doc())
   

def get_parameters(method):
   spec = args(method)
   parameters =  ([spec.varargs] if spec.varargs is not None else []) + spec.args + spec.kwonlyargs
   parameters = [el for el in parameters if el != 'self']
   #defaults = spec.defaults if spec.defaults is not None else spec.kwonlydefaults.values() if spec.kwonlydefaults is not None else []
   #lp, ld = len(parameters), len(defaults)
   #defaults = [None] * (lp - ld) + list(defaults)
   #return [(parameters[i], defaults[i]) for i in range(lp)]
   return parameters#, defaults


class documentation_class(): # a list of method_class objects
    "It contains the doc-strings of all the main plotext functions."

    def __init__(self):
      self._methods = []

    def _add_method(self, name, alias = ''):
      method = method_class(name, alias)
      self._methods.append(method)
      setattr(self, name, method.show)

    def _last(self):
      return self._methods[-1]

    def _set_doc(self, doc):
       self._last().set_doc(doc)
  
    def _add_parameter(self, name, doc = '', type = '', default = ''):
      self._last().add_parameter(name, doc, type, default)

    def _set_output(self, doc = '', type = ''):
       self._last().set_output(doc, type)

    def _get_method(self, name):
      names = [el.name for el in self._methods]
      if name not in names:
          print(warning, 'no method', name + '() found')
      return self._methods[names.index(name)] if name in names else None

    def _get_parameters(self, parameter, method):
       method = self.get_method(method)
       return method.get_parameters(parameter) if method is not None else None

    def _add_past_parameter(self, name, method, default = None):
       method = self._get_method(method)
       parameter = method.get_parameter(name) if method is not None else None
       parameter = parameter if default is None else parameter.copy(default)
       self._last().append_parameter(parameter) if parameter is not None else None

    def _set_past_output(self, method):
       method = self.get_method(method)
       output = method.output
       self._set_output(output.type, output.doc)

    def all(self):
      docs = (nl * 3).join([el.get_title() + nl + el.get_doc() for el in self._methods if el.status in [0, 1]])
      print(docs)

    def _add_function(self, function):
      name = function.__name__
      method = self._get_method(name)
      name += '()'
      if method is None:
         print(warning, name, "doc not present")
         return
      doc = method.get_doc()
      function.__doc__ = uncolorize(doc)
      function.doc = lambda: print(doc)
      parameters_actual = get_parameters(function)
      parameters_found = method.get_parameters()
      if parameters_actual != parameters_found:
          actual = colorize(cm.join(parameters_actual), style = 'italic')
          found = colorize(cm.join(parameters_found), style = 'italic')
          print(warning, "the parameters of", name, "are", actual, "not",  found + '.')

          
class parameter_types():
   def __init__(self):
      self.int = 'an integer'
      self.float = 'a float'
      self.num = 'a number'
      self.str = 'a string'
      self.bool = 'a Boolean'

      
      self.ints = 'integers'
      self.floats = 'floats'
      self.nums = 'numbers'
      self.strs = 'strings'
      self.bools = 'Booleans'

      self.list_int = lambda n = 'many': self.plural(self.ints, n) 
      self.list_float = lambda n = 'many': self.plural(self.floats, n) 
      self.list_num = lambda n = 'many': self.plural(self.nums, n) 
      self.list_str = lambda n = 'many': self.plural(self.strs, n) 
      self.list_bool = lambda n = 'many': self.plural(self.bools, n)

      self.fig = 'a plotext figure'
      self.xy = 'one or two lists of numbers or string dates'
      self.multiple_xy = 'an optional list of numbers or date strings and a mandatory matrix of numbers'
      self.x = 'a list of numbers or string dates'
      self.marker = 'a string or a list of strings'
      self.color = 'a string or an integer (from 0 to 255) or a tuple of 3 integers (from 0 to 255)'
      self.colors = 'strings or integers (from 0 to 255) or tuples of 3 integers (from 0 to 255)'
      self.list_color = lambda n = 'many': self.plural(self.colors, n)
      self.color_list = self.color + ' or a list of those'
      self.str_list = self.mix(self.str, self.list_str())
      
      self.str_int = self.mix(self.str, self.int)
      self.str_num = self.mix(self.str, self.num)
      self.list_str_num = lambda n = 'many': self.plural(self.mix(self.strs, self.nums), n)
      self.list_num_bool = lambda n = 'many': self.plural(self.mix(self.nums, self.bools), n)
      self.bool_num_str = self.mix(self.bool, self.num, self.str)
      self.dic = "a dictionary with mandatory keys: 'Open', 'Close', 'High', 'Low'; each value should be a list of numbers."
      self.matrix = 'a list of numbers or a list of tuples 3 integers (from 0 to 255)'
      self.datetime = 'a datetime object'
      self.list_datetime = self.plural(self.datetime)
      self.data = 'a 2 dimensional matrix of numbers or strings'

   def plural(self, type, n = 'many'):
      return 'a list of ' + (str(n) + sp if not isinstance(n, str) else '') + type

   def mix(self, *types):
      return ' or '.join(types)
   
documentation = documentation_class()
method = documentation._add_method
doc = documentation._set_doc
par = documentation._add_parameter
past = documentation._add_past_parameter
out = documentation._set_output
past_out = documentation._set_past_output
add = documentation._add_function

t = parameter_types()
