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

#3A). 
"""
a.	Open the mystats.py file (uploaded to Canvas as part of this homework) for editing and running with Python.  You will see that mystats.py mostly consists of comments describing functions that you will need to write, with a single uncommented print() function call that displays the name of the module itself.

print('The current module is:', __name__)

Run the module, and add a comment after the print() function call describing the output when mystats.py is the main module, that is, the module that you are currently editing and testing.



