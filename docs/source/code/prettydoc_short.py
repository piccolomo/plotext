from plotext.prettydoc import docs

def mean(par1 = 1, par2 = 2):
	return (par1 + par2) / 2 

average = mean

def harmonic_mean(par1 = 1, par2 = 3):
	return (par1 * par2) ** 0.5

pd = docs()
add = pd.add_function
alias = pd.add_alias
doc = pd.add_doc
par = pd.add_parameter
spec = pd.add_parameter_spec
past = pd.add_past_parameter
out = pd.add_output
past_out = pd.add_past_output
update = pd.update
show = pd.show

add(mean)
doc("This string describes my mean() function in general")
alias("average")
par("par1", "the first parameter"); spec('float', 1)
par("par2","the second parameter"); spec('float', 2)
out('the mean of the input parameters', 'float')

add(harmonic_mean)
doc("This string describes my harmonic_mean() in general")
past("par1", 'mean')
past("par2", 'mean'); spec('float', 3)
out('the harmonic mean of the input parameters', 'float')

update()
show()