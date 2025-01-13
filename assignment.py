def format_string(name, age):
    """
    Create a formatted string using f-strings.
    Args:
        name (str): Person's name
        age (int): Person's age
    Returns:
        str: Formatted string
    """
    return f"My name is {name} and I am {age} years old"

#the function format_string is passed its value to the variable format_message
formatted_message = format_string("Alice",30)
print(formatted_message)


def conditional_check(number):
    """
    Check if a number is greater, lesser, or equal to 10.
    Args:
        number (int): Number to check
    Returns:
        str: "Greater", "Lesser", or "Equal"
    """
    if number > 10:
        return "Greater"
    elif number < 10:
        return "Lesser"
    else:
        return "Equal"
    
#the function is called for execution
print(conditional_check(15))  # Output: "Greater"
print(conditional_check(5))   # Output: "Lesser"
print(conditional_check(10))  # Output: "Equal"


def loop_sum(n):
    """
    Calculate sum of numbers from 1 to n using a loop.
    Args:
        n (int): Upper limit
    Returns:
        int: Sum of numbers
    """
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

print(loop_sum(5))  #total = (1 + 2 + 3 + 4 + 5)


def list_operations(numbers):
    """
    Perform operations on a list of numbers.
    Args:
        numbers (list): List of numbers
    Returns:
        tuple: (sum, max, min)
    """
    total = sum(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    return (total,maximum,minimum)

numbers = [1,3,5,7,9] #defining the list of numbers
result =  list_operations(numbers) #calling out function for execution
print(result)


def dict_operations(students_dict):
    """
    Find students with scores above 80.
    Args:
        students_dict (dict): Dictionary of student names and scores
    Returns:
        list: Names of students with scores > 80
    """
    # Use a list comprehension to filter students with scores > 80
    return [name for name, score in students_dict.items() if score > 80]
# dictionary of studenta names and score
students = {
    "John": 85,
    "Alice": 90,
    "Bob": 75,
    "Eve": 95
}
result = dict_operations(students)
print(result)


def set_operations(list1, list2):
    """
    Find common elements between two lists.
    Args:
        list1 (list): First list
        list2 (list): Second list
    Returns:
        set: Common elements
    """
    # Convert both lists to sets and find their intersection
    return set(list1) & set(list2)

list1 = [1, 2, 3]
list2 = [2, 3, 4]
result = set_operations(list1, list2)
print(result)  



def arithmetic_ops(a, b):
    """
    Perform arithmetic operations.
    Args:
        a (float): First number
        b (float): Second number
    Returns:
        dict: Results of arithmetic operations
    """
    return {
    "sum": a + b,
    "difference": a - b,
    "product": a * b,
    "quotient": a / b if b != 0 else None,  # Handle division by zero
    }
result = arithmetic_ops(10, 5)
print(result)


def logical_ops(x, y):
    """
    Perform logical operations.
    Args:
        x (bool): First boolean
        y (bool): Second boolean
    Returns:
        dict: Results of logical operations
    """
    return {
        "and": x and y,       
        "or": x or y,         # Logical OR
        "not_x": not x,       
        "not_y": not y,          
    }

result = logical_ops(True, False)
print(result)

def bitwise_ops(a, b):
    """
    Perform bitwise operations.
    Args:
        a (int): First integer
        b (int): Second integer
    Returns:
        dict: Results of bitwise operations
    """
    return {
        "and": a & b,          # Bitwise AND
        "or": a | b,           # Bitwise OR
        "xor": a ^ b,          # Bitwise XOR
    }
result = bitwise_ops(12, 10)
print(result)