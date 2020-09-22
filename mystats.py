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
    for item in num: 

        if is_iter(item):
            totalSum += sum(item)
            count += len(item)
        else:
            totalSum += item
            count += 1

    return totalSum/count

# define the stddev function here

def stddev(*num):
    average = mean(mean(num))
    totalSum = 0.0
    count = 0
    for item in num: 
        eachSum = 0.0
        eachLength = 0
        if is_iter(item):
            for i in item:
                eachSum += (i-average)**2
            eachLength += len(item)
        else:
            totalSum += (item-average)**2
            count += 1
        totalSum += eachSum
        count += eachLength
    return (totalSum/(count-1))**0.5

# define the median function here
def median(*num):
    num = np.sort(num)
    for item in num: 
        if is_iter(item):
            if(len(num[0])%2 == 0):
                lower_index = int(len(num[0])/2-1)
                upper_index = int(len(num[0])/2)
                return (num[0][lower_index]+num[0][upper_index])/2
            else:
                return num[0][int((len(num[0])-1)/2)]
        else:
            if(len(num)%2 == 0):
                return (num[len(num)/2-1]+num[len(num)/2])/2
            else:
                return num[int((len(num)-1)/2)]



# define the mode function here

def mode(*num):
    for item in num:
        if is_iter(item):
            
        else:

# part (a)
print('The current module is:', __name__)
# The current module is: __main__

# part (b)

print('mean(1) should be 1.0, and is:', mean(1))
print('mean(1,2,3,4) should be 2.5, and is:', mean(1,2,3,4))
print('mean(2.4,3.1) should be 2.75, and is:', mean(2.4,3.1))
#print('mean() should FAIL:', mean())

# part (c)


v1 = {1, 2, 3}     # a set is iterable
print(v1, "is iterable:", is_iter(v1))
v2 = 123
print(v2, "is iterable:", is_iter(v2))

print('mean([1,1,1,2]) should be 1.25, and is:', mean([1,1,1,2]))
print('mean((1,), 2, 3, [4,6]) should be 3.2,' + 'and is:', mean((1,), 2, 3, [4,6]))

# part (d)
# your code here

for i in range(10):
    print("Draw", i, "from Norm(0,1):",
                        np.random.randn())
    
ls50 = [ v1 for v1 in np.random.randn(50)] 
print("Mean of", len(ls50), "values from Norm(0,1):",
                        mean(ls50))
ls10000 = [ v2 for v2 in np.random.randn(10000)] 

print("Mean of", len(ls10000), "values from " +
           "Norm(0,1):", mean(ls10000))


# part (e)
# your code here
np.random.seed(0)

a1 = np.array(np.random.randn(10))
print("a1:", a1)    # should display an ndarray of 10 values

print("the mean of a1 is:", mean(a1))

# part (f)
# your code here


print("the stddev of a1 is:", stddev(a1))
# part (g)
# your code here

print("the median of a1 is:", median(a1))
print("median(3, 1, 5, 9, 2):", median(3, 1, 5, 9, 2))

# part (h)
# your code here


print("mode(1, 2, (1, 3), 3, [1, 3, 4]) is:", mode(1, 2, (1, 3), 3, [1, 3, 4]))
