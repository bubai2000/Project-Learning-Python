# Lists need not be homogeneous i.e. each element can be of different type, even a list can be member of another list
# Building and using a list
# Refer to https://www.geeksforgeeks.org/python-list/
list1 = []  # Declaring a list
while True:
       f=int(input("Enter 1 to add item in grocery list, 2 to insert item in the middle, 3 to remove using item number, 4 to "
           "remove item using name, 5 to reverse the list, 6 to sort list in alphabetical(or numeric) order, 7 to print the list,"
           "0 to exit =>"))
       if(f==1):
              x=input("Enter item name:")
              list1.append(x) # We can use extend() to add multiple items at once Note: Both append and extend adds item at last
              print("Item added successfully!")
       if(f==2):
              x=int(input("Enter position=>"))
              y=input("Enter item to add=>")
              x=x-1
              list1.insert(x,y)
              print("Item added successfully!")
       if(f==3):
              x=int(input("Enter position of item in list=>"))
              x=x-1
              list1.pop(x) # By default pop() deletes last element
              print("Removed successfully!")
       if(f==4):
              x=input("Enter item to delete=>")
              try:
                     list1.remove(x)
                     print("Deleted successfully!")
              except:
                     print("Item not found!")    # Handling ValueError Exception
       if(f==5):
              list1.reverse()
              print("List in reverse order=>", list1)
       if(f==6):
              list1.sort()
              print("Sorted list=>", list1)
       if(f==7):
              print(list1)
       if(f==0):
              break

"""
Python item indexing:
1. Positive indexing: Starting element(from left to right) has index 0, and increases with each element
2. Negative indexing: -1 refers to the last item, -2 refers to the second-last item

Slicing of a list: 
To print elements from beginning to a range use [: Index], 
to print elements from end-use [:-Index], to print elements from specific Index till the end use [Index:], 
to print elements within a range, use [Start Index:End Index] 
and to print the whole List with the use of slicing operation, use [:]. 
Further, to print the whole List in reverse order, use [::-1]
Try other things like [<Index 1>:<Index 2>:<Hopping limit>]
"""