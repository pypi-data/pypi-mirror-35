def jackknife_stats(theta_subs, theta_full, N=None, d=1):
    """Compute Jackknife Estimates, SE, Bias, t-scores, p-values
    
    Parameters:
    -----------
    theta_subs : ndarray
        The metrics, estimates, parameters, etc. of 
        the model (see "func") for each subsample.
        It is a <C x M> matrix, i.e. C=binocoeff(N,d) 
        subsamples, and M parameters that are returned  
        by the model.
    
    theta_full : ndarray
        The metrics, estimates, parameters, etc. of 
        the model (see "func") for the full sample.
        It is a <1 x M> vecotr with the M parameters 
        that are returned by the model.
    
    N : int
        The number of observations in the full sample.
        Is required for Delete-d Jackknife, i.e. d>1.
        (Default is N=None)
    
    d : int
        The number of observations to leave out for 
        each Jackknife subsample, i.e. the subsample
        size is N-d. (The default is d=1 for the 
        "Delete-1 Jackknife" procedure.)    
    
    Returns:
    --------
    pvalues : ndarray
        The two-sided P-values of the t-Score for each 
        Jackknife estimate. 
        (In Social Sciences pval<0.05 is referred as 
        acceptable but it is usually better to look 
        for p-values way closer to Zero. Just remove 
        or replace a variable/feature with high 
        pval>=pcritical and run the Jackknife again.)
    
    tscores : ndarray
        The t-Score for each Jackknife estimate. 
        (As rule of thumb a value abs(tscore)>2 indicates 
        a bad model parameter but jsut check the p-value.)
    
    theta_jack : ndarray
        The bias-corrected Jackknife Estimates (model 
        parameter, metric, coefficient,  etc.). Use the 
        parameters for prediction.

    se_jack : ndarray
        The Jackknife Standard Error
    
    theta_biased : ndarray
        The biased Jackknife Estimate.

    
    Other Variables:
    ----------------
    These variables occur in the source code as 
    intermediate results.

    Q : int 
        The Number of independent variables of 
        a model (incl. intercept).

    C : int
        The number of Jackknife subsamples if d>1.
        There are C=binocoeff(N,d) combinations.
    
    """
    #The biased Jackknife Estimate
    import numpy as np
    theta_biased = np.mean(theta_subs, axis=0);
    
    #Inflation Factor for the Jackknife Standard Error
    if d is 1:
        if N is None: N = theta_subs.shape[0];
        inflation = (N - 1) / N;
    elif d>1:
        if N is None: raise Exception("If d>1 then you must provide N (number of observations in the full sample)")
        C = theta_subs.shape[0];
        inflation = ((N - d) / d) / C;
    
    #The Jackknife Standard Error
    se_jack = np.sqrt( inflation * np.sum((theta_subs - theta_biased)**2, axis=0) );
    
    #The bias-corrected Jackknife Estimate
    theta_jack = N * theta_full - (N-1) * theta_biased ;
    
    #The Jackknife t-Statistics
    tscores = theta_jack / se_jack;
    
    #Two-sided P-values
    import scipy.stats;
    Q = theta_subs.shape[1];
    pvalues = scipy.stats.t.sf(np.abs(tscores), N-Q-d)*2;
    
    #done
    return pvalues, tscores, theta_jack, se_jack, theta_biased






def jackknife_print(pvalues, tscores, theta_jack, se_jack, theta_biased=None, theta_fullsample=None, varnames=None, N=None, d=None):
    #Title
    title = '\n';
    if d: title += 'Delete-'+str(d)+' ';
    title += 'Jackknife';
    if N: title += ', N='+str(N);
    if d and N: 
        if d>1: 
            import scipy.special; 
            title += ', C(N,d)='+str(scipy.special.comb(N,d, exact=True))
    print(title)

    #column headers
    slen = 9
    fs0 = '{:32s}' + ''.join(['{:^'+str(slen+2)+'s}' for _ in range(len(pvalues))])
    if varnames:
        print(fs0.format('', *[v[:slen] for v in varnames]))
    else:
        print(fs0.format('', *['Var'+str(v) for v in range(len(pvalues))]))

    #first columns format
    s0 = '{:>30s}: '
    #data columns' format
    sn1 = '{:8.3f}   ';
    sn2 = '  {:8.5f} ';
    fs1 = s0 + ''.join([sn1 for _ in range(len(pvalues))])
    fs2 = s0 + ''.join([sn2 for _ in range(len(pvalues))])
    print(fs2.format('p-Values', *list(pvalues)))
    print(fs2.format('t-Scores', *list(tscores)))
    print(fs2.format('Jackknife Standard Error (SE)', *list(se_jack)))
    print(fs1.format('Jackknife Estimates (theta)', *list(theta_jack)))
    if theta_biased is not None:
        print(fs1.format('Jackknife Biased Estimate', *list(theta_biased)))
    if theta_fullsample is not None:
        print(fs1.format('Full Sample Estimate', *list(theta_fullsample)))

    #print('\n')
    return None