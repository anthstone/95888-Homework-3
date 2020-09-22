"""
Anno Zhang
Anthony Stone
Team 16
"""
#1a
fin = open('expenses.txt', 'rt', encoding = 'utf-8') 
records = []
for line in fin:
    records.append(line.strip())
    
for line in records:
		    print(line)
fin.close

#1b
fin = open('expenses.txt', 'rt', encoding = 'utf-8')
records2 = [line.strip() for line in fin]
print("\nrecords == records2:", records == records2, '\n')
fin.close

#1c
fin = open('expenses.txt', 'rt', encoding = 'utf-8')
records3 = tuple(tuple(line.strip().split(sep=":") for line in fin))
for tup in records3:
		    print(tup)
            
fin.close

#1d
cat_set = {tup[1] for tup in records3[1:]} 
date_set = {tup[2] for tup in records3[1:]} 


print('Categories:', cat_set, '\n')
print('Dates:     ', date_set, '\n')

#1e
rec_num_to_record = {k: v for (k, v) in zip(range(len(records3)),records3)}


for rn in range(len(rec_num_to_record)):
		    print('{:3d}: {}'.format(rn, rec_num_to_record[rn]))

for i in rec_num_to_record.items():
		    print('{:3d}: {}'.format(i[0], i[1]))
            
            
#2). Variadic Functions
"""
You will need to modify the file mystats.py for this part of the homework, 
since we will use mystats.py as a module to import in part 3 of the homework.  
Your mystats.py file must be included in the .zip archive that you upload when 
you have completed this homework.

HINT: It is cheating to implement your mean function by calling the mean 
function from some other library/module.  Write your own code!  Check 
Wikipedia, Wolfram, or elsewhere to make sure you have the correct formulas.
"""

#2A). []
"""
GO TO MYSTATS.PY

"""

#2B).
"""
Define the function mean() below the relevant comment. The mean() function 
should take one or more positional parameters, and return the arithmetic mean 
of its arguments when called. Uncomment these test statements in mystats.py to 
test that your mean() function is working correctly:

print('mean(1) should be 1.0, and is:', mean(1))
print('mean(1,2,3,4) should be 2.5, and is:',
                                    mean(1,2,3,4))
print('mean(2.4,3.1) should be 2.75, and is:',
                                    mean(2.4,3.1))
print('mean() should FAIL:', mean())

Run the module and confirm success.  (Comment out the last of these four 
print() calls after you have confirmed that calling mean() with no argument 
fails.)
"""

#2C). []
"""
Improve your mean() function so that it accepts numeric iterables as well as 
individual numeric values as arguments. To test whether a variable refers to an 
iterable, you can call the iter() function. iter() will fail and raise an 
exception if its argument is not iterable.  Here is a function that uses 
try/except to test whether an object is iterable without crashing your program:

def is_iter(v):
    v_is_iter = True
    try:
        iter(v)
    except:
        v_is_iter = False
    return v_is_iter

v1 = {1, 2, 3}     # a set is iterable
print(v1, "is iterable:", is_iter(v1))
v2 = 123
print(v2, "is iterable:", is_iter(v2))

Hint: If v refers to an iterable, then sum(v) is the sum of the values in the 
iterable, and len(v) is the length of the iterable.  You can use these to help 
with your implementation of your improved mean() function.

Uncomment these test statements in mystats.py to test that your improved mean() 
function is working correctly. (The test print() functions from part (b) should 
also continue to work, except of course for the call of main() with no 
argument, which should be commented out.)

print('mean([1,1,1,2]) should be 1.25, and is:',
                               mean([1,1,1,2]))
print('mean((1,), 2, 3, [4,6]) should be 3.2,' +
      'and is:', mean((1,), 2, 3, [4,6]))

Run the module and confirm success.
"""

#2D). []
"""
d.	At the top of your mystats.py file, insert the line:

import numpy as np

so that we can use NumPy’s random number generator functions.  (We will do more
with NumPy in part (3) below.)

np.random.randn() with no argument will return a single random draw from the
standard Normal distribution (mean 0.0, standard deviation 1.0, often represented in
writing as Norm(0,1)).  Add this code to the end of your program to display ten
draws from Norm(0,1):

for i in range(10):
    print("Draw", i, "from Norm(0,1):",
                        np.random.randn())

At the end of your program, use list comprehension to create a list of 50 draws from
Norm(0,1).  Then, test your mean() function on this list, like this:

ls50 = ... list comprehension ...
print("Mean of", len(ls50), "values from Norm(0,1):",
                        mean(ls50))

The displayed mean should be “close to” 0.0.  If the random number generator is
“truly random" then the mean should tend closer to 0.0 as the number of draws in
the sample increases.  Perform another test using 10,000 draws, like this:

ls10000 = ... list comprehension ...
print("Mean of", len(ls10000), "values from " +
           "Norm(0,1):", mean(ls10000))

Is the displayed mean “closer to” 0.0 than before?  Of course, this is a casual test, not
a rigorous test.
"""

#2E). []
"""
We can set the seed value for the random number generator with:
	
np.random.seed(seed)

Set the seed to 0, then create an ndarray of 10 random draws from Norm(0,1) as we
illustrated in lecture.  Add this code at the end of your program; run the module and
confirm success.

a1 = np.random.randn(10)
print("a1:", a1)    # should display an ndarray of 10 values

An ndarray object is iterable, so your mean() functions should process a1 just fine.
Add this code at the end of your program, then run the module.

print("the mean of a1 is:", mean(a1))

Since you set the seed to 0.0 prior to this, you should get the same value that I do:
0.7380231707288347
"""

#2F). []
"""
Define the stddev() function to compute the sample standard deviation of its arguments, where the arguments can be the same as those passed to the mean() function.  Add this code at the end of your program, then run the module.
	
print("the stddev of a1 is:", stddev(a1))

If you have defined stddev() correctly, you should get the same value that I do:
1.0193909949356386
"""

#2G). []
"""
Define the median() function to compute the median of its arguments, where the arguments can be the same as those passed to the mean() function.  Add this code at the end of your program, then run the module.
	
print("the median of a1 is:", median(a1))

If you have defined median() correctly, you should get the same value that I do:
0.6803434597319808

Then, add this code at the end of your program, and run the module.
	
print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))

If you have defined median() correctly, you should get 3.
"""

#2H). []
"""
h.	Define the mode() function to compute the mode of its arguments, where the 
arguments can be the same as those passed to the mean() function.  The mode is 
usually used with integer counts, rather than floating point values.  Since a 
data set can be multimodal (that is, have two or more values that each occur 
“most often”), your mode() function should return a tuple of modal values.  
Hint:  You may find a dict useful for keeping track of how often each value 
occurs. You can use v in d to test whether v is a key in dictionary d.

Add this code at the end of your program, then run the module.
	
print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:",
            mode(1, 2, (1, 3), 3, [1, 3, 4]))

If you have defined mode() correctly, you should get either (1, 3) or (3, 1), since
1 and 3 each occur 3 times in the argument list, whereas 2 and 4 only occur one
time each.
"""


#3 Modules []

#3A).
"""
Open the my_stat_test.py file (uploaded to Canvas as part of this homework) for 
editing and running with Python.  You will see that my_stat_test.py contains 
several tests of the functions that you developed in mystats.py, such as:

print("mean of int_list1:", ms.mean(int_list1))

It also makes use of some more random number generator functions, rand() and 
randint(), that you should learn about in the Python NumPy documentation.

Add an appropriate import statement at the top of my_stat_test.py so that 
mystats.py is imported with the abbreviated name ms.  Run the my_stat_test.py 
module.  You should see that it works, but all of the testing code in 
mystats.py is also executed when mystats.py is imported.  This is not the 
behavior that an importer of a library expects.
"""

#3B). []
"""
b.	Modify mystats.py so that its testing code is only executed when 
mystats.py is the main module.  Then, run my_stat_test.py as the main module, 
and confirm that although the functions defined in mystats.py are available in 
my_stat_test.py, the testing code in mystats.py is not executed when mystats.py 
is imported.
"""

#4 NumPY

#4A). []
"""
a.	In lecture, we introduced NumPy and its N-dimensional array type, ndarray.  
We looked at ways to create ndarray objects, and at three ways for accessing 
rows/columns/sections of an ndarray: slices, Boolean indexes, and “fancy” or 
integer indexes.

There is much more to NumPy than we have time to talk about.  In Python for 
Data Analysis, 2nd Ed., read through sections 4.2: Universal Functions, 
4.3: Array-Oriented Programming, and 4.4: File Input and Output, and try out 
all of the examples in a Jupyter notebook.
"""



