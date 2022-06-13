"""
[Week 1 - Session 1]

Problem #1 Reverse a String
"""

"""
UNDERSTAND:
-Is the user input always going to be string?
-> First assume that it is
-empty string should just print out empty string

MATCH:
-indexing string from the back and concatenating

PLAN:
-Create a new empty string
-Using a simple for loop that indexing from the last index of the string
-Add each character as the for loops reads from the back
-Return the new string
"""

#Implement

#Solution 1: O(n^2) runtime
def reverse1(string):
    reversed = ""
    for i in range(len(string)-1,-1,-1):
        reversed+=string[i]
    return reversed

#Solution 2: O(n) runtime using an array and two pointers
def reverse2(string):
    arr = list(string)
    first, last = 0, len(string)-1
    while(first<last):
        temp = arr[first]
        arr[first] = arr[last]
        arr[last] = temp
        first, last = first+1, last-1
    return "".join(arr) 


def main():
    print(reverse2(input("Enter a string: ")))

main()