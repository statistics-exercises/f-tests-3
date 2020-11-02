# Histogram

OK now that we can sample from this distribution lets see if we can characterise the distribution.  __To complete this task you need to use the outline code on the right to generate a histogram by repeatedly taking samples from the distribution that was introduced in the previous task with `N1=5` and `N2=5`.__

The outline code that I have written calls on you to copy the function  (`generate_f_variable`) that you wrote for the previous task. This function will be used to generate the random variable that we are interested in.  I have then created and stored the midpoints for a series of histogram bins that start at `xmin` and that finish at `xmax` in a NumPy array called `xvals`.  Your task is to write a loop that generates 200 random variables using the  `generate_f_variable` function and the parameters above.  Within this loop, you should use the NumPy array called `counts` to count how many of these random variables fall within each of the `nbins` histogram bins.  

Once you have generated all your random variables you will need to normalise the histogram that is stored in `counts`.   When your code is complete it should generate a graph showing the histogram that you have generated in red.    

__Make sure you look at the graph that is generated.  Does the approximate probability density function you have computed resemble any of the distributions that you have learned about thus far in this course?__
