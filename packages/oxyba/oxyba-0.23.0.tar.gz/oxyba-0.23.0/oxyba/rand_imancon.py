
def rand_imancon(x, rho):
    """Iman-Conover Method to generate random ordinal variables

    x : ndarray
        <obs x cols> matrix with "cols" ordinal variables
        that are uncorrelated.
    
    rho : ndarray
        Spearman Rank Correlation Matrix
    
    Links
    * Iman, R.L., Conover, W.J., 1982. A distribution-free approach to 
        inducing rank correlation among input variables. Communications 
        in Statistics - Simulation and Computation 11, 311–334. 
        https://doi.org/10.1080/03610918208812265
    * Mildenhall, S.J., 2005. Correlation and Aggregate Loss Distributions 
        With An Emphasis On The Iman-Conover Method 101. (Page 45-49)

    """
    import numpy as np
    from scipy.stats import norm 
    import oxyba as ox
    import warnings

    warnings.warn("This implementation of the the Iman-Conover methods is not working properly. Please check if 'Y=ox.rand_imancon(X,C)' are close to the target correlation C. For example 'Cnew=ox.corr_tau(Y)' and 'np.abs(C - Cnew)'. ")

    #data prep
    n,d = x.shape

    #vector with Inverse CDF values 
    # Notes: Mildenhall (2005) scales `a` to 1.920616465815559 
    # but such transformation will not change the ranks lateron.
    a = norm.ppf(np.arange(1,n+1)/(n+1));

    #start loop to shuffle these invcdf values for each column
    M = np.nan * np.empty((n,d));
    M[:,0] = a; #fixed assigned
    for k in range(1,d):
        np.random.shuffle(a); 
        M[:,k] = a;

    #Ordering T
    # Notes: Mildenhall (2005, p.51) refers to a covarance matrix
    #   but displays a correlation matrix. On p.46 he refers to 
    #   a correlation matrix but supplies the formula of a 
    #   covariance matrix E=np.dot(M.T,M)/n. The sample cov would
    #   be E=np.dot(M.T,M)/(n-1) or E=np.cov(M)
    #   Using a cov would E to be NOT semipositive definite!
    E = np.corrcoef(M,rowvar=0);  #corrected
    F = np.linalg.cholesky(E).T;
    invF = np.linalg.inv(F);
    C = np.linalg.cholesky(rho).T; #checked
    T = np.dot(M, np.dot(invF,C)); #checked

    #get the ordered indicies of T
    idx = np.argsort(T, axis=0);
    #this would remove any preexisting correlation!
    X = np.sort(x, axis=0); 
    #rerank X
    Y = np.nan * np.empty((n,d));
    for k in range(0,d):
        Y[:,k] = X[idx[:,k],k]

    #done
    return Y
