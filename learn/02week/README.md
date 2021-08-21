# Week 2

- For Loops
  - Introduction to For Loops
    - [video](https://youtu.be/O_bopOVtG8A)
    - repeat a block of code a fixed number of times

```python
iv = iteration_variable
start = init_value_of_iv
stop = max_value_of_iv
for <iv> in range(start, stop, step):
   #code block to be iterated

```
   - range() could be any iterable value(string, list, tuple)

  - For Loop Control
    - [video](https://youtu.be/Jq3tlwBcLXU)
    - `break` and `continue`
    - `continue` means skip
  - Exercise: For Loops Using range()
    - [video](https://youtu.be/VxiK1SiP4qo)
    - [forloop_range.py](forloop_range.py)
  - Code Challenge: `for` loop1
    - [cc_for_loop1.py](cc_for_loop1.py)
  - Code Challenge: `for` loop2
    - [cc_for_loop2.py](cc_for_loop2.py)
  - Code Challenge: `for` Loop Loading Bar
    - [cc_loading_bar.py](cc_loading_bar.py)
  - Code Challenge: Star Staircase `for` Loop
    - [cc_staircase_loop.py](cc_staircase_loop.py)
- Python Functions
  - Introduction to Python Functions
    - [video](https://youtu.be/Sx5ZKoaudoQ)
    - DRY, opposite of WET
    - organize code
    - divide and conquer?
  - Exercise: Built-In Functions
    - [video](https://youtu.be/J2PdIJLS_7I)
  - Exercise: Converting User Input
    - [video](https://youtu.be/5Tk4rOgyGh4)
    - `str(arg)`
    - `int(arg)`
    - `float(arg)`
  - Exercise: Creating Your Own Functions
    - [video](https://youtu.be/HlfHNm9ESkw)
  - Void & Value-Returning Functions
    - [video](https://youtu.be/-sN34UiUsTw)
    - `return` is like `break`
  - Local and Global Scope
    - [video](https://youtu.be/nrXAMG-mnkE)
    - variable scope - where a variable can be accessed
    - python function have local scope
    - global variables can be accessed from everywhere
  - Lambda Functions
    - [video](https://youtu.be/_cARe8MRImc)
    - aka anonymous functions
    - can only return one expression
    - *higher-order function*: functions that take functions as arguments
    - *callback functions*: functions used by higher-order functions as arguments
    - lambda functions are used as callbacks
  - Exercise: Introduction to Recursion
    - [video](https://youtu.be/cB4P0RZhh8k)
    - *recursive function*: a function that calls(invokes) itself.
    - recursive functions must have a *base condition* that will stop the recursion.
- Code Challenge: Reverse name
  - [cc_reverse.py](code/cc_reverse.py)
- Modules and Packages
  - Introduction to Modules and Packages
    - [video](https://youtu.be/BrVm9PVy4uA)
    - *module*: aka a python file. collection of related code
    - *package*: collections of related modules
  - Exercise: Creating Modules
    - [video](https://youtu.be/4HfOnZcLJBs)
    - [my_module.py](./code/my_module.py)
    - [use_module.py](./code/use_module.py)
  - Exercise: Creating Packages
    - [video]()
- The Random Module
  - Three Ways to Randomize
    - [video](https://youtu.be/5blTKuj7Mbk)
    - `randint()`
    - `choice()`
    - `shuffle()`
  - Exercise: Using Random
    - [video](https://youtu.be/gNZDXGSq5RM)
    - [randomize.py](code/randomize.py)
- Code Challenge: Dice Game
  - [cc_dicegame.py](code/cc_dicegame.py)
- Week 2 Quiz
- Portfolio Project: Your Game Algorithm
- Week 2 Workshop 
  - [scope.py](code/lecture/scope.py)
  - LEGB
    - local
    - enclosing
    - global
    - built-in
  - [lambda.py](code/lecture/lambda.py)
    - lambda aka anonymous
  - [recursion.py](code/lecture/recursion.py)
