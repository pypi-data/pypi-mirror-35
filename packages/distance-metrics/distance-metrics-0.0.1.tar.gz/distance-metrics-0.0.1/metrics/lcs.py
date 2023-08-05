import numpy as np

def bakkelund(u, v):
	""" Compute the bakkelund distance between vectors u and v.
		The bakkelund distance is defined as 1 - LCS(u, v) / M(u, v). Where
		 - LCS(u, v) is the length of the longest common subsequence of u and v;
		 - M(u, v) is the length of the longest vector between u and v.
		
		Parameters
		----------
		u : (N,) array_like
			Input vector of features of u. Used to compute distance to v.
			
		v : (N,) array_like
			Input vector of features of v. Used to compute distance to u.
			
		Returns
		-------
		result : float
			Bakkelund distance between `u` and `v`.
			
		"""
	# Transform input to numpy arrays if not given
	u = np.asarray([x for x in u])
	v = np.asarray([x for x in v])
	
	# Perform checks
	if u.ndim > 1 or v.ndim > 1:
		raise ValueError("Input vector `u` should be 1-D.")
	
	# Return the bakkelund distance
	return 1. - llcs(u, v) / max(u.shape[0], v.shape[0])

def llcs(u, v):
	""" Quickly compute the length of the longest common
		subsequence between vectors u and v.
		
		Realise a small speedup for finding length of longest common subsequence
		Speedup is achieved by the following heuristics (NB: resulting value
		will still be the same as regular LLCS):
			- Find common subsequences at start and ending (as these will always
			  be in the LLCS, this can be found in O(n) and shortens the
			  input lengths for the remaining O(n²) computation.
			- Remove elements not present in both inputs (as these can never be
			  in the LLCS) This can be found in O(n) and shortens the input
			  lengths for the remaining O(n²) computation.
		
		Parameters
		----------
		u : (N,) array_like
			Input vector of features of u. Used to compute length of LCS with v.
			
		v : (N,) array_like
			Input vector of features of v. Used to compute length of LCS with u.
			
		Returns
		-------
		result : float
			Length of LCS between `u` and `v`.
		"""
	# Initialise start match index
	start, end = 0, 0
	# Increase start until non-match is found starting from 0
	i = 0
	while i < min(len(u), len(v)) and u[i] == v[i]:
		start += 1
		i     += 1
	# Increase end until non-match is found starting from end
	i = 0
	while i > 0 and u[-i] == v[-i]:
		end += 1
		i   += 1
	# Set length of matching indices
	matches = min(start + end, len(u), len(v))
	# Set the remainder of u and v
	u = u[start:-end or len(u)]
	v = v[start:-end or len(v)]
	# Get elements present in both inputs
	elements = set(u) & set(v)
	# Remove all elements not present in both inputs while retaining order
	# This is possible because an element not in both inputs cannot be in the
	# longest common subsequence.
	u = np.array([x for x in u if x in elements])
	v = np.array([x for x in v if x in elements])	
	# Return # matches at start + LLCS of remainder without uniqes
	return matches + _llcs_(u, v)

def _llcs_(u, v):
	""" Compute the length of the longest common
		subsequence between vectors u and v.
				
		Parameters
		----------
		u : (N,) array_like
			Input vector of features of u. Used to compute length of LCS with v.
			
		v : (N,) array_like
			Input vector of features of v. Used to compute length of LCS with u.
			
		Returns
		-------
		result : float
			Length of LCS between `u` and `v`.			
		"""		
	# Get input lengths
	m = u.shape[0]
	n = v.shape[0]
	
	# Construct a 
	table = np.zeros((m+1, n+1))
	
	# Compute all lengths of common subsequences
	for i in range(1, m+1):
		for j in range(1, n+1):
			if u[i-1] == v[j-1]:
				table[i, j] = table[i-1, j-1] + 1
			else:
				table[i, j] = max(table[i, j-1], table[i-1, j])
				
	# Return length of longest common subsequence
	return table[-1, -1]
