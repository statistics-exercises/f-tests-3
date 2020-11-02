import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_histogram(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        dx = this_x[1] - this_x[0]
        for i in range(len(this_x)) :
            l, u = this_x[i] - 0.5*dx, this_x[i] + 0.5*dx
            p = scipy.stats.f.cdf(u,5,5) - scipy.stats.f.cdf(l,5,5)
            var = p*(1-p)
            confl = scipy.stats.norm.ppf(0.01,loc=0,scale=np.sqrt(var))
            confu = scipy.stats.norm.ppf(0.99,loc=0,scale=np.sqrt(var))
            self.assertTrue( this_y[i]*dx > confl and this_y[i]*dx < confu, "your histogram does not appear to be correct" )
            
    def test_f_generation(self) :
        for i in range(2,5) :
            for j in range(2,5) :
                t = gen_f_variable( i, j )
                pval = scipy.stats.f.cdf( t, i-1, j-1 )
                self.assertTrue( pval>0.005 and pval<0.995, "your gen_f_variable function does not appear to be sampling from the correct distribution" )
                
    def test_normalisation(self) :
        fighand=plt.gca()
        figdat = fighand.get_lines()[0].get_xydata()
        this_x, this_y = zip(*figdat)
        self.assertTrue( np.abs( sum(this_y)*(this_x[1]-this_x[0]) - 1 )<1e-7, "your histogram has not been normalised correctly" )
    
