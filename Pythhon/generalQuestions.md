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

# Q 10. What will be the output of the following code? Explain why.

```python
my_dict = {"a": 1, "b": 2}
my_dict["a"] = 5
print(my_dict)  # {"a": 5, "b": 2}
```
