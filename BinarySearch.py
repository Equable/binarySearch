import sys
import math

def binarySearch(data, find):
    left = 0
    right = len(data)
    curr = None
    print("Looking for: ", find)
    print("In the following list: ", data)
    while left <= right:
        curr = math.floor((left + right)/2)
        if find == data[curr]:
            found = True
            break
        elif find < data[curr]:
            right = curr
        else:
            left = curr
    if found:
        print("Found a match at index: ", curr)
    else:
        print("No Match Found")

        
tobesearched = ["Carlos", "Shiv", "Louis", "Frank", "Mike", "Toby", "Keith", "Johnny", "Alice", "Timothy"]
tobesearched.sort()
searchFor = "Shiv"
binarySearch(tobesearched, searchFor)
found = None