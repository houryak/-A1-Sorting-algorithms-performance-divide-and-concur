# 1-Chocolate Distribution Algorithm:
# class to represent a chocolate with its weight, price, and type
class Chocolate:
    # initialize the attributes of the chocolate object
    def __init__(self, student, weight, price, type):
        self.student = student
        self.weight = weight
        self.price = price
        self.type = type

    def __str__(self):
        return f"{self.student} {self.type} chocolate ({self.weight}gm, {self.price} AED)"
        # return the string representation of the chocolate object


# using an iterative approach to distribute chocolates to students
def distribute_chocolates_iterative(chocolates, students):
    # creates an empty list to store the distributed chocolates
    distributed_chocolates = []
    '''Using the modulo operator, it assigns a chocolate from the chocolates list to
    each student as iterates through the students list, making ensuring that 
    each chocolate is given out just once.'''
    for i in range(len(students)):
        distributed_chocolates.append(chocolates[i % len(chocolates)])
    # return the list of distributed chocolates
    return distributed_chocolates


'''
Using a recursive approach to distribute chocolates to students
It initializes an empty list to store the distributed chocolates.
It checks if there are no more students left. If so, it returns an empty list.
It checks if the current student index is equal to the length of the students list. If so, it returns an empty list.
It recursively calls itself with the remaining students and increments the index.
It appends the chocolate at the current index (modulo the length of the chocolates list) 
to the distributed chocolates list.
It returns the list of distributed chocolates.
'''
def distribute_chocolates_recursive(chocolates, students, index=0):
    if len(students) == 0:
        return []
    if index == len(students):
        return []
    distributed_chocolates = distribute_chocolates_recursive(chocolates, students[index+1:], index+1)
    distributed_chocolates.append(chocolates[index % len(chocolates)])
    return distributed_chocolates

# Test Cases
'''
These test cases demonstrate the usage of both functions with sample input data.
The chocolates list contains three Chocolate objects, each with a weight, price, type, and student assigned to it.
The students list contains the names of the students who will receive the chocolates.
The distribute_chocolates_iterative and distribute_chocolates_recursive functions a
re called with the chocolates and students lists as input.
The distributed chocolates are printed for each algorithm using a loop.
'''
chocolates = [Chocolate('Alice', 10, 5, 'Milk'),
              Chocolate('Bob', 8, 4, 'Dark'),
              Chocolate('Cathy', 12, 6, 'White')
              ]
students = ['Alice', 'Bob', 'Cathy']
distributed_chocolates_iterative = distribute_chocolates_iterative(chocolates,students)
distributed_chocolates_recursive = distribute_chocolates_recursive(chocolates,students)
print("TEST CASE FOR PART 1")
print("Iterative Distribution Algorithm:")
for chocolate in distributed_chocolates_iterative:
    print(chocolate)
print("\nRecursive Distribution Algorithm:")
for chocolate in distributed_chocolates_recursive:
    print(chocolate)
# COMPLEXITY ANALYSIS
'''
Iterative Distribution Algorithm:
Time complexity: O(n), where n is the number of students.
Space complexity: O(1), since we don't create any new data structures during iteration.
Best case: When all students have unique chocolates, the algorithm performs exactly n assignments.
Average case: Assuming random distributions of chocolates among students, the algorithm would 
still perform approximately n assignments per student.
Worst case: When all chocolates are identical, the algorithm needs to check every chocolate for each student, 
resulting in n * m assignments, where m is the total number of chocolates.


Recursive Distribution Algorithm:
Time complexity: O(n), similar to the iterative version.
Space complexity: O(log n) due to the recursive call stack.
Best case: Same as the iterative version.
Average case: Similar to the iterative version.
Worst case: As mentioned above, when all chocolates are identical,
the algorithm requires n * m assignments, which is worse compared to the iterative version.
'''
# 2-Sorting the Chocolates:
# class use to represent a chocolate with its weight, price, type, and the student it is assigned to
class Chocolate:
    #initializes the attributes of the chocolate object, including the student it is assigned to.
    def __init__(self, student, weight, price, type):
        self.student = student
        self.weight = weight
        self.price = price
        self.type = type

    #returns a string representation of the chocolate object.
    def __str__(self):
        return f"{self.student}-{self.type} chocolate({self.weight}gm, {self.price} AED)"

    # a list of chocolates and a list of students as input and returns a list of distributed chocolates.
    def distribute_chocolates(self, chocolates, students):
        distributed_chocolates = []
        for i in range(len(students)):
            distributed_chocolates.append(chocolates[i % len(chocolates)])
        return distributed_chocolates

#a list of chocolates as input and returns a list of chocolates sorted by weight
    def sort_by_weight(self, chocolates):
        return sorted(chocolates, key=lambda x:x.weight)

# a list of chocolates as input and returns a list of chocolates sorted by price.
    def sort_by_price(self, chocolates):
        return sorted(chocolates, key=lambda x:x.price)

# Test case


'''
The chocolates list contains three Chocolate objects, each with a weight, price, type, and student assigned to it.
The students list contains the names of the students who will receive the chocolates.
An instance of the Chocolate class is created to call the instance methods.
The distribute_chocolates, sort_by_weight, and sort_by_price methods 
are called with the chocolates and students lists as input.
The distributed chocolates and sorted chocolates are printed using a loop.
'''
chocolates = [Chocolate('Alice', 10, 5, 'Milk'),
              Chocolate('Bob', 13, 4, 'Dark'),
              Chocolate('Cathy', 12, 6, 'White')
              ]
students = ['Alice', 'Bob', 'Cathy']

# Create an instance of Chocolate to call the instance methods
choco_instance = Chocolate("Test", 1, 1, "test")
distributed_chocolates = choco_instance.distribute_chocolates(chocolates, students)
sorted_in_weight = choco_instance.sort_by_weight(distributed_chocolates)
sorted_in_price = choco_instance.sort_by_price(distributed_chocolates)

print("\nTEST CASE FOR PART 2")
print("Distributed chocolates:")
for chocolate in distributed_chocolates:
    print(chocolate)

print("\nChocolates that are sorted by weight:")
for chocolate in sorted_in_weight:
    print(chocolate)

print("\nChocolates that are sorted by price:")
for chocolate in sorted_in_price:
    print(chocolate)

# 3. Searching for a Specific Chocolate:
import bisect


# class to represent a chocolate object with attributes for student name, weight, price, and type.
class Chocolate:
# initializes the attributes of the chocolate object when it is created.
    def __init__(self, student, weight, price, type):
        self.student = student
        self.weight = weight
        self.price = price
        self.type = type

# Placeholder method without implementation to distribute chocolates among students.
    def distribute_chocolates(self, chocolates, students):
        pass

# Sorts a list of chocolate objects based on their weights in ascending order.
# Uses the sorted function with a lambda key function to sort the chocolates by weight.
    def sort_by_weight(self, chocolates):
        return sorted(chocolates, key=lambda x: x.weight)

# Sorts a list of chocolate objects based on their prices in ascending order.
# Utilizes the sorted function with a lambda key function to sort the chocolates by price.
    def sort_by_price(self, chocolates):
        return sorted(chocolates, key=lambda x: x.price)


# Performs a binary search on a sorted list of chocolate objects to find a specific target value (price or weight).
def binary_search(arr, start, end, target, attr="price"):
# Recursively divides the search range based on the target value and the specified attribute (default is price).
    if start > end:
        return None
    mid = (start + end) // 2
    current_val = getattr(arr[mid], attr)
    if current_val == target:
        return arr[mid].student
    elif current_val < target:
        return binary_search(arr, mid + 1, end, target, attr)
    else:
        return binary_search(arr, start, mid - 1, target, attr)

# Implements a binary search algorithm to find the student holding a chocolate with a specified price or weight.
def find_student_by_price_or_weight(chocolates, target, attr="price"):
# Searches through a sorted list of chocolates based on the specified attribute (default is price).
    start = 0
    end = len(chocolates) - 1
#Returns the student name if a chocolate with the target price or weight is found, otherwise returns None.
    while start <= end:
        mid = (start + end) // 2
        if getattr(chocolates[mid], attr) == target:
            return chocolates[mid].student
        elif getattr(chocolates[mid], attr) < target:
            start = mid + 1
        else:
            end = mid - 1

    return None


# Test case
'''
Creates a list of chocolate objects with different attributes for testing purposes.
Calls the binary_search function to find students holding chocolates with specific prices or weights.
Prints out the results of each search query for verification and testing purposes.
'''
chocolates = [Chocolate('Alice', 10, 15, 'Milk'),
              Chocolate('Bob', 13, 4, 'Dark'),
              Chocolate('Cathy', 12, 6, 'White'),
              Chocolate('David', 9, 7, 'Strawberry'),
              Chocolate('Emma', 14, 8, 'Green Tea')
              ]

print('\nTEST CASE FOR PART 3')
find_result_price = binary_search(chocolates, 0, len(chocolates) - 1, 7, attr="price")
print(f"Student holding chocolate with price 7: {find_result_price}")

find_result_weight = binary_search(chocolates, 0, len(chocolates) - 1, 12, attr="weight")
print(f"Student holding chocolate with weight 12: {find_result_weight}")

find_result_invalid = binary_search(chocolates, 0, len(chocolates) - 1, 15, attr="price")
print(f"Student holding chocolate with price 15: {find_result_invalid}")






