from plotext.prettydoc import docs

# Dummy arithmetic mean of two numbers (used to showcase prettydoc)
def mean(par1 = 1, par2 = 2):
	return (par1 + par2) / 2

average = mean

# Dummy harmonic-mean-like function of two numbers (used to showcase prettydoc)
def harmonic_mean(par1 = 1, par2 = 3):
	return (par1 * par2) ** 0.5

pd = docs()
add  = pd.function
doc  = pd.description
par  = pd.parameter
past = pd.past_parameter
out  = pd.output

past_out, update = pd.past_output, pd.update

add(mean)
doc("This string describes my mean() function in general", alias = "average")
par("par1", "the first parameter", 'float', 1)
par("par2", "the second parameter", 'float', 2)
out('the mean of the input parameters', 'float')

add(harmonic_mean)
doc("This string describes my harmonic_mean() in general")
past("par1", 'mean')
past("par2", 'mean', 'float', 3)
out('the harmonic mean of the input parameters', 'float')

update()
harmonic_mean.doc()
