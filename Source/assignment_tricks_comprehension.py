name=["Soumyadip","Sounak","Sumit"]
numbers=[1,2,3,4]

# List comprehension
name_upper=[n.upper() for n in name]

name_len=[len(n) for n in name]

# Dictionary comprehension
name_len_dict={n: len(n) for n in name}

even=[n for n in numbers if n%2==0] # Similar to filter

print(name_upper)
print(name_len)
print(name_len_dict)
print(even)