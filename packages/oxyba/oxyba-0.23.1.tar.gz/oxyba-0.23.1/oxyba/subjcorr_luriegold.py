
def subjcorr_luriegold(R):
    """Lurie-Goldberg Algorithm to adjust a correlation matrix to be semipositive definite

    Philip M. Lurie and Matthew S. Goldberg (1998), An Approximate Method
       for Sampling Correlated Random Variables from Partially-Specified
       Distributions, Management Science, Vol 44, No. 2, February 1998, pp
       203-218, URL: http://www.jstor.org/stable/2634496
    """
    import numpy as np
    import scipy.optimize

    #subfunctions
    def xtotril(x, idx, mat):
        """Create 'L' lower triangular matrix."""
        mat[idx] = x;
        return mat;
    
    def xtocorr(x, idx, mat):
        L = xtotril(x, idx, mat);
        C = np.dot(L, L.T);
        return C, L;
    
    def objectivefunc(x, R, idx, mat):
        C,_ = xtocorr(x, idx, mat);
        f = np.sum((R - C)**2);
        return f
    
    def nlcon_diagone(x, idx, mat):
        C,_ = xtocorr(x, idx, mat);
        return np.diag(C) - 1;
    
    #dimension of the correlation matrix
    d = R.shape[0]
    n = int((d**2 + d)/2.);

    #other arguments
    mat = np.zeros((d,d)); #the lower triangular matrix without values
    idx = np.tril(np.ones((d,d)),k=0) > 0; #boolean matrix
    #idx = np.tril_indices(d,k=0); #row/col ids (same result)

    #start values of the optimization are Ones
    x0 = np.ones(shape=(n,)) / n;

    #for each of the k factors, the sum of its d absolute params values has to be less than 1
    condiag = {'type': 'eq', 'args': (idx, mat), 'fun' : nlcon_diagone};

    #optimization
    algorithm = 'SLSQP'
    opt = {'disp': False}
    
    #run the optimization
    results = scipy.optimize.minimize(
        objectivefunc, x0, 
        args = (R, idx, mat),
        constraints = [condiag],
        method=algorithm, options=opt)
    
    #Compute Correlation Matrix
    C, L = xtocorr(results.x, idx, mat);
    
    #done
    return C, L, results

