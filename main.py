import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

def gen_f_variable( N1, N2 ) : 
  # Your code to generate the variable that we introduced in the previous task goes here
  

# This generates the midpoints of all your histogram bins
nbins, xmin, xmax = 10, 0, 20 
delx = (xmax - xmin ) / nbins
xvals, counts = np.zeros(nbins), np.zeros(nbins)
for i in range(nbins) : xvals[i] = xmin + i*delx

# Add code to generate the histogram here 




# You should not need to modify anything from here onwards
# This plots the histogram you have generated
plt.plot( xvals, counts, 'r-')
plt.savefig("histogram_t.png")
