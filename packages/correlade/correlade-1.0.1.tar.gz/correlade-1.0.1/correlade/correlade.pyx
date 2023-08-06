"""
Author: Ian Coleman
Purpose: Distance Correlation matrix and graphic for Pandas

TODO:
change dist_corr to a self method
change subset_of to length of df
add graphic element 
replace the dcor package with the actual formula and code
documentation to be fitted to standards
check what happens in edge cases e.g string in df
number of chars on each line

Next things to do
Make seaborn a dependency
Make users not have to install cython
Only import the heatmap part of seaborn
"""

import pandas as pd
from sys import argv
import seaborn as sns
import distcorr



cpdef dcorr (df, graph=None, obs=0):
	"""

	Master function

	Creates matrix of distance correlation values for each pairing of columns
	in the provided dataframe

	If there are more than 2000 rows or columns, a random selection of 2000
	are used for the calculation

	Parameters:
	df --> a dataframe of numerical values
	graph --> give any int here if you want a heatmap of the correlation matrix

	"""

	matrix = dcorr_matrix(df, obs)
	print(matrix)

	if graph is not None:
		matrix_heatmap(matrix)


cpdef dcorr_matrix (df, obs):
	"""
	Creates matrix of distance correlations
	"""

	# Make empty df to house correlation values
	matrix = pd.DataFrame(index = df.columns, columns = df.columns)
	
	# Ensure no more than 2000 rows, use number provided if any
	if obs == 0:
		obs = df.shape[0]
	cols = df.shape[1]

	if obs > 2000:
		df = df.sample(2000)
	else:
		df = df.sample(obs)
	
	if cols > 2000:
		df = df.sample(2000, axis = 1)

	cdef int no_rows = df.shape[0]
	cdef int no_cols = df.shape[1]
	cdef int x, y

	print('AAAAAAAAA: ', no_rows)

	for x in range(0,no_cols):
		for y in range(0,no_cols):
			matrix.iloc[y,x] = distcorr.distcorr(df.iloc[0:no_rows, x], df.iloc[0:no_rows, y])

	return matrix


def matrix_heatmap (matrix):
	"""
	Creates heatmap of correlation matrix with Seaborn
	"""
	
	# Convert all to floats as required by Seaborn graphing
	matrix = matrix.transform(lambda x: x.astype('float64'))
	print('Attempting graph --> assuming Pandas in Jupyter')
	print(sns.heatmap(matrix))  