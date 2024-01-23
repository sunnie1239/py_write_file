#data = [0,1,2,3,4,5]
data = range(10)
#print(data)
with open('test.txt', 'w') as f:
	for d in data:

		f.write(str(d) + '\n')

