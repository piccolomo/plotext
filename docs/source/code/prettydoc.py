from plotext.prettydoc import docs

# Dummy arithmetic mean of two numbers (used to showcase prettydoc)
def mean(par1 = 1, par2 = 2):
	return (par1 + par2) / 2

average = mean

# Dummy harmonic-mean-like function of two numbers (used to showcase prettydoc)
def harmonic_mean(par1 = 1, par2 = 3):
	return (par1 * par2) ** 0.5

pd = docs() # new prettydoc container

pd.function(mean) # it adds the 'mean' function to docs
pd.description("This string describes my mean() function in general", alias = "average") # it adds some basic function documentation, and an alias
pd.parameter("par1", "the first parameter", 'float', 1) # it adds the first parameter documentation: name, basic doc, type and default value
pd.parameter("par2", "the second parameter", 'float', 2)
pd.output('the mean of the input parameters', 'float') # it adds the 'main' output documentation: basic doc and type 

pd.function(harmonic_mean)
pd.description("This string describes my harmonic_mean() in general")
pd.past_parameter("par1", 'mean') # it recycle the documentation of a parameter of the 'mean' function 
pd.past_parameter("par2", 'mean', 'float', 3) # a past parameter type and default value can be changed once imported
pd.output('the harmonic mean of the input parameters', 'float')

pd.update()
harmonic_mean.doc()
