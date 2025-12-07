
district_of_BD = ["Dhaka", "Chittagong", "Rajshahi",  "Khulna", "Barishal", "Sylhet", "Rangpur", "Mymensingh"]


print(district_of_BD[0])            # prints first item (index 0)
print(district_of_BD[-1])           # prints last item using negative index

district_of_BD[0] = "Dacca"         # updates/changes the first item
print(district_of_BD)

district_of_BD.append("LaLaLand")   # adds one new item at the end
print(district_of_BD)

district_of_BD.extend(["Noakhali","Cumilla"])     # adds multiple items at the end

indexing = district_of_BD.index('Khulna')         # finds the index number of 'Khulna'
print(indexing)

district_of_BD.reverse()             # reverses the entire list order
print(district_of_BD)


district_of_BD.sort()                # sorts the list alphabetically
print(district_of_BD)

district_of_BD.clear()              # removes all elements from the list
print(district_of_BD)

fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruit = fruits.count('apple')          # counts how many times "apple" appears
print(fruit)