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

# Binary search algo

def binary_search(list, searchVal):
    lower = 0
    upper = len(list) - 1
    
    searching = True
    index = -1
    while searching:
        mid = upper - (upper - lower) // 2
        if mid <= lower or mid >= upper: #finished search without finding value
            
            searching = False
        print("Searched cell: " + str(mid))
        if searchVal ==  list[mid]:
            #searchVal must equal list[mid]
            print("Found!")
            index = mid
            searching = False
        elif searchVal > list[mid]:
            lower = mid + 1
        elif searchVal < list[mid]:
            upper = mid - 1
        
    return index



#def binary_search(list, searchkey):


newlist = make_list()
for i in newlist:
    print(i)

searchVal = int(input("Enter number to search for: "))
foundIndex = binary_search(newlist, searchVal)
if foundIndex > -1:
    print("I found " + str(searchVal) + " at index: " + str(foundIndex))
else:
    print("Value not found")

