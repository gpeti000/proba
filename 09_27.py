import numpy as np

def generated_uncorrelated_returns(expected_returns, vols, numOfPath):
    a_exp_rets = np.array(expected_returns) - (np.array(vols) ** 2) / 2
    numofassets = len(expected_returns)
    rets = np.random.normal(a_exp_rets, vols, (numOfPath, numofassets)) #np.random.normal(átlag, szórás, darabszám)
    return rets

def test_generated_uncorrelated_returns(expected_returns, vols, numOfPath):
    a_exp_rets = np.array(expected_returns) - (np.array(vols) ** 2) / 2
    numofassets = len(expected_returns)
    rets = np.random.normal(a_exp_rets, vols, (numOfPath, numofassets)) #np.random.normal(átlag, szórás, darabszám)
    return rets

def correlated_std_norm(corr_mat, numOfPath):
    a_corr = np.array(corr_mat)
    a_l = np.linalg.cholesky(a_corr)
    numofassets = a_corr.shape[0]
    a_uncorr = np.random.normal(size=(numOfPath, a_l.shape[0]))
    #check correlation structure
    a_corr = np.dot(a_uncorr, a_l.transpose())
    return a_corr

def test_correlated_std_norm():
    corr_mat = [[1.0, -.8], [-.8, 1.0]]
    a_corr = correlated_std_norm(corr_mat, 100000)
    print(np.corrcoef(a_corr.transpose()))

def correlated_norm(exp_values, stds, corr_mat, numOfPath):
    a_corr = correlated_std_norm(corr_mat, numOfPath)
    a_res = a_corr * np.array(stds) + np.array(exp_values)
    return a_res

def test_correlated_norm():
    exp_values = [0.08, 0.0495]
    stds = [0.2, 0.1]
    corr_mat = [[1.0, -.8], [-.8, 1.0]]
    a_res = correlated_norm(exp_values, stds, corr_mat, 2000)
    print(a_res.mean(axis=0))
test_correlated_norm()


rs = [0.1, 0.05] #átlagok
vols = [0.2, 0.01] #szórások
numOfPath = 200 #darabszám
a_rets=generated_uncorrelated_returns(rs, vols, numOfPath)
#print(a_rets.mean(axis=0)) #oszloponkénti átlag
