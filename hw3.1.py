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


