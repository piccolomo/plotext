from plotext.prettydoc import docs

# Dummy arithmetic mean of two numbers (used to showcase prettydoc)
def mean(par1 = 1, par2 = 2):
	return (par1 + par2) / 2

average = mean

# Dummy harmonic-mean-like function of two numbers (used to showcase prettydoc)
def harmonic_mean(par1 = 1, par2 = 3):
	return (par1 * par2) ** 0.5

pd = docs() # new prettydoc container

pd.add_function(mean) # it adds the 'mean' function to docs
pd.add_doc("This string describes my mean() function in general") # its adds some basic function documentation 
pd.add_alias("average") # it adds an alias
pd.add_parameter("par1", "the first parameter") # it adds the first parameter documentation: name, and basic doc
pd.add_parameter_spec('float', 1)
pd.add_parameter("par2", "the second parameter")
pd.add_parameter_spec('float', 2)
pd.add_output('the mean of the input parameters', 'float') # it adds the 'main' output documentation: basic doc and type 

pd.add_function(harmonic_mean)
pd.add_doc("This string describes my harmonic_mean() in general")
pd.add_past_parameter("par1", 'mean') # it recycle the documentation of a parameter of the 'mean' function 
pd.add_past_parameter("par2", 'mean')
pd.add_parameter_spec('float', 3) # a past parameter type and default value can be changed once imported
pd.add_output('the harmonic mean of the input parameters', 'float')

pd.update()
pd.show()