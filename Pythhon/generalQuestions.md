# Q1. What is difference between stack memory and heap memory?

## Stack memory

- Stack memory is used for function calls
- local variables and control flow (if, loops), memory allocation and deallocation are automatic
- Follow LIFO
- Fast access becuase memory is managed directly by the system
- **Lifetime -** Exists only while the function is executing

```python
"""

"""
```

## Heap memory

- It is used for dynamically allocating memory
- Memory is allocated and freed manually (or by garbage collector in some languages)
- Slower than stack becuase management is more complex
- **Lifetime -** Exists until explicitly freed.

```python
```

## Key differences
<!-- table -->

# Q2. What is difference between `==` and `=` in programming?

# Q3. What is a variable, why do we need variables in programming?

- A variable is a named memory location used to store data.
- We use variables to store, reuse and maniplate data in a program.
- Variables make code readable and manageable.

```python
a = 5
print(a)
```

# Q4. What is the difference between a mutale and immutable data types? Give one example each.

- Mutable data tpes are those whose values can be changed after **creation** without changing their memory location.

- Immutable data types are those whose values after **creation**. Any change will create new data in a new memory location.

# Q5. What is the difference between list and tuple? Give three examples.

# Q6. What is a loop? Why do we use in programming?

- A loop is a control structure used to execute a block of repeatedly until a condition a satisfied.
- We use loops to reduce code repetition and automate repetetive tasks
- For loops are used for iteration on a collection on a data (dict, list, tuple)
- While loop is used only for condition.

# Q7. What will be the output of the following code, and why?

```python
x = 10
y = x
y = 20
print(x)    # 10
```

# Q8. What is the difference between `break` and `continue` in a loop?

- `break` is used to **terminate** the loop completely when a condition is met.
- `continue` is used to **skip** the current iteration and move to the next one.

# Q9. What is a dictionary in python? How is it different from a list?

- A dict in python is a data structure used to store data in key-value pairs.
- It allows fast access to values using unique keys.

# Q10. What will be the output of the following code? Explain why.

```python
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 5
print(my_dict)  # {"a": 5, "b": 2}
```

# Q11. What is the difference between `is` and `==` in python?

- `==` checks whether two values are equal
- `is` checks whether two variables or values are referring to the same **memory location**

## Example

- Never use `string` or `integer` in example for `is` and `==`
- Always use `list` with same `integer` values

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)
print(a is b)
```

# Q12. Write a python program to check whether a number is even or odd.

```python
def numChecker(num):
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")

numChecker(2)   # even
numChecker(3)   # odd
```

# Q13. What is a function and why do we use functions in programming?

# Q14. What is the difference between a parameter and an argument in functions?

# Q15. What is an exception? How do you handle exceptions in python? Give a short example.

- An exception is a runtime error that occurs during program execution.
- In python exceptions are handled using `except`, `else` and `finally` blocks

```python
try:
    result = 5/0
except ZeroDivisionError:
    print("A number cannot be devided by zero")
```
# Q16. What is difference between compile time error and runtime error?

# Q17. What is difference between compiler and an interpreter.

- Compiler translates the entire source code into machine code **before** execution.
- Interpreter translates and executes the code **line by line during** execution.
- Interpreter executes code without generating a separate compiled file.

# Q18. Difference between shallow copy and deep copy in python

# Q19. What is a set in python? Mention two important properties of set.

# Q20. What is the difference a list and a set in python. Mention at least three differences.
