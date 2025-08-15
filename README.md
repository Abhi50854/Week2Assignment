# Python List Manipulation Example

This is a simple Python program that demonstrates basic operations on a list, including adding elements, updating elements, removing elements, sorting, and finding the index of an element.

## Features

The code demonstrates the following operations:

1. **Create an empty list**

   ```python
   my_list = []
   ```

2. **Add elements to the list** using `append()`

   ```python
   my_list.append(10)
   my_list.append(20)
   my_list.append(30)
   my_list.append(40)
   ```

3. **Update an element** in the list

   ```python
   my_list[1] = 15  # Changes the second element from 20 to 15
   ```

4. **Add more elements** to the list

   ```python
   my_list.append(50)
   my_list.append(60)
   my_list.append(70)
   ```

5. **Remove the last element** using `pop()`

   ```python
   my_list.pop()
   ```

6. **Sort the list** in ascending order

   ```python
   my_list.sort()
   ```

7. **Find the index of an element**

   ```python
   index_of_30 = my_list.index(30)
   ```

## Output

When the program is run, it prints the state of the list after each operation:

```
The list is: [10, 20, 30, 40]
The updated list is: [10, 15, 30, 40]
The final list is: [10, 15, 30, 40, 50, 60, 70]
After popping the last element, the list is: [10, 15, 30, 40, 50, 60]
The sorted list is: [10, 15, 30, 40, 50, 60]
The index of 30 is: 2
```

## How to Run

1. Make sure Python is installed on your system.
2. Save the code in a file called `list_example.py`.
3. Open a terminal or command prompt.
4. Run the program:

   ```bash
   python list_example.py
   ```
