# Building and using a dictionary
book = {}  # Declaring a dictionary variable values are stored as "Key": "Value"
while 1:
    f = int(input("Enter 1 to add student(s), 2 to view all student list, 3 to search student name using roll no., "
                  "4 to see student roll numbers, \n 5 to delete a student entry, 6 to update entry,"
                  "7 to delete register, 0 to exit=>"))
    if f == 1:
        a = int(input("Enter how many students to add=>"))
        for i in range(a):
            x = input("Enter student roll number=>")
            n = input("Enter student name=>")
            book.update({x: n})  # Updates the dictionary with the specified key-value pairs, also adds new
            print("Student added successfully!")

    elif f == 2:
        print(book)
        a = book.values()  # Returns a list of all the values in the dictionary, we can do list operations on that
        print(a)
        b = book.items()  # Returns a list containing a tuple for each key value pair
        print(b)
    elif f == 3:
        x = input("Enter student roll number to search=>")
        n = book.get(x)  # Returns the value of the specified key returns "None" if key is invalid
        if n == None:
            print("Student details not found! see available roll numbers")
        else:
            print("Student name is=>", n)
    elif f == 4:
        print("Registered student roll nos.=>", book.keys())  # Returns a list containing the dictionary's keys
    elif f == 5:
        x = input("Enter student roll number to delete=>")
        n = book.get(x)
        if n:
            book.pop(x)  # Removes the element with the specified key,
            # if key is invalid throws "KeyError", by default deletes index -1, i.e. last entry
            print("Record deleted successfully!")
        else:
            print("Student record not found! See available roll numbers")
    elif f == 6:
        x = input("Enter student roll number=>")
        n = input("Enter student name=>")
        book.update({x: n})
        print("Record updated successfully!")
    elif f == 7:
        book.clear()  # clear()	Removes all the elements from the dictionary
        print("Register deleted successfully")
    elif f == 0:
        break
    else:
        print("Please enter a valid choice!")
# Some extra function
# setdefault() Returns the value of the specified key. If key does not exist: insert the key, with the specified value
# copy()	Returns a copy of the dictionary
# fromkeys()	Returns a dictionary with the specified keys and value
# popitem()	Removes the last inserted key-value pair
