# Create an array with values in it
# Search array for value specified by user input

def make_list():
    upperBound = int(input("input upper bound: "))
    lowerBound = 0
    list = [0]
    while list[-1] < upperBound:
        list.append(list[-1] + 2)
    if list[-1] > upperBound:
        del list[-1]
    return list

#def binary_search(list, searchkey):


newlist = make_list()
for i in newlist:
    print(i)

