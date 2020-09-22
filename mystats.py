#2A). 
"""
Open the mystats.py file (uploaded to Canvas as part of this homework) for
editing and running with Python.  You will see that mystats.py mostly consists
of comments describing functions that you will need to write, with a single 
uncommented print() function call that displays the name of the module itself.

print('The current module is:', __name__)

Run the module, and add a comment after the print() function call describing 
the output when mystats.py is the main module, that is, the module that you are
currently editing and testing.
"""


import numpy as np
# File: mystats.py

# define the mean function here
def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

def mean(*num):
    totalSum = 0.0
    count = 0
    if is_iter(num) is True:
        print('aaaa',num[0],num,len(num))
        return sum(num)/len(num)
    for n in num: 
        totalSum += n
        count += 1
    return totalSum/count

# define the stddev function here

# define the median function here

# define the mode function here

# part (a)
print('The current module is:', __name__)
# The current module is: __main__

# part (b)
# print('mean(1) should be 1.0, and is:', mean(1))
# print('mean(1,2,3,4) should be 2.5, and is:',
#                                     mean(1,2,3,4))
# print('mean(2.4,3.1) should be 2.75, and is:',
#                                     mean(2.4,3.1))
# print('mean() should FAIL:', mean())

# part (c)
# print('mean([1,1,1,2]) should be 1.25, and is:',
#                                mean([1,1,1,2]))
# print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
#       'and is:', mean((1,), 2, 3, [4,6]))

# part (d)
# your code here

# part (e)
# your code here

# part (f)
# your code here

# part (g)
# your code here

# part (h)
# your code here
