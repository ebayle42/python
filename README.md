![OUROBOROS](https://github.com/ebayle42/python/blob/master/ouroboros.gif)

*This repository has been created as part of the 42 curriculum by ebayle.*

# python

## Description

This repository is all you have to know about the Python Module in 42 curriculum

## Modules

- `python_module_00`    : First module of python, Python Fundamentals Through Garden Data
- `python_module_01`    : Second module of python, Object-Oriented Garden Systems
- `python_module_02`    : Third module of python, Data Engineering for Smart Agriculture
- `python_module_03`    : Fourth module of python, Mastering Python Collections
- `python_module_04`    : Fifth module of python, Digital Preservation in the Cyber Archives
- `python_module_05`    : Sixth module of python, Polymorphic Data Streams in the Digital Matrix
- `python_module_05bis` : Sixth bis module of python, Packages, Environments and the Alchemist’s Toolchain
- `python_module_06bis` : Seventh bis module of python, from Data Streams to Battle Strategies
- `python_module_09`    : Tenth module of python, Discover Pydantic Models & Validation
- `python_module_10`    : Eleventh module of python, python fundamentals through garden data

## Instructions

Compile:

```sh
python3 main.py
```

Run mypy:

```sh
mypy main.py
```

Run flake8
```sh
flake8 main.py
```

Run pyvision:

```sh
pyvision -m 00
```

## Details

### python_module_00 — Python Fundamentals Through Garden Data

<details>
<summary><b>ex0</b> — ft_hello_garden.py</summary>

| | |
|---|---|
| **Exercise** | `ex0` |
| **Directory** | `python_module_00/ex0/` |
| **File(s)** | `ft_hello_garden.py` |
| **Function / Class** | `ft_hello_garden()` |
| **Description** | Prints `Hello, Garden Community!` |
| **Concepts** | Defining a function, `print()` |

</details>

<details>
<summary><b>ex1</b> — ft_garden_name.py</summary>

| | |
|---|---|
| **Exercise** | `ex1` |
| **Directory** | `python_module_00/ex1/` |
| **File(s)** | `ft_garden_name.py` |
| **Function / Class** | `ft_garden_name()` |
| **Description** | Asks for a garden name and prints it with its status |
| **Concepts** | `input()`, printing multiple values |

</details>

<details>
<summary><b>ex2</b> — ft_plot_area.py</summary>

| | |
|---|---|
| **Exercise** | `ex2` |
| **Directory** | `python_module_00/ex2/` |
| **File(s)** | `ft_plot_area.py` |
| **Function / Class** | `ft_plot_area()` |
| **Description** | Reads a length and a width and prints the plot area |
| **Concepts** | Casting with `int()`, arithmetic |

</details>

<details>
<summary><b>ex3</b> — ft_harvest_total.py</summary>

| | |
|---|---|
| **Exercise** | `ex3` |
| **Directory** | `python_module_00/ex3/` |
| **File(s)** | `ft_harvest_total.py` |
| **Function / Class** | `ft_harvest_total()` |
| **Description** | Reads the harvest of 3 days and prints the total |
| **Concepts** | Multiple inputs, addition |

</details>

<details>
<summary><b>ex4</b> — ft_plant_age.py</summary>

| | |
|---|---|
| **Exercise** | `ex4` |
| **Directory** | `python_module_00/ex4/` |
| **File(s)** | `ft_plant_age.py` |
| **Function / Class** | `ft_plant_age()` |
| **Description** | Tells if a plant is ready to harvest (age > 60 days) |
| **Concepts** | `if` / `else` conditions |

</details>

<details>
<summary><b>ex5</b> — ft_water_reminder.py</summary>

| | |
|---|---|
| **Exercise** | `ex5` |
| **Directory** | `python_module_00/ex5/` |
| **File(s)** | `ft_water_reminder.py` |
| **Function / Class** | `ft_water_reminder()` |
| **Description** | Reminds to water the plants if the last watering was more than 2 days ago |
| **Concepts** | Conditions, comparison operators |

</details>

<details>
<summary><b>ex6</b> — ft_count_harvest_iterative.py / ft_count_harvest_recursive.py</summary>

| | |
|---|---|
| **Exercise** | `ex6` |
| **Directory** | `python_module_00/ex6/` |
| **File(s)** | `ft_count_harvest_iterative.py`<br>`ft_count_harvest_recursive.py` |
| **Function / Class** | `ft_count_harvest_iterative()`<br>`ft_count_harvest_recursive()` |
| **Description** | Counts the days until harvest then prints `Harvest time!`, once with a `for` loop and once with a nested recursive function |
| **Concepts** | `for` + `range()`, recursion |

</details>

<details>
<summary><b>ex7</b> — ft_seed_inventory.py</summary>

| | |
|---|---|
| **Exercise** | `ex7` |
| **Directory** | `python_module_00/ex7/` |
| **File(s)** | `ft_seed_inventory.py` |
| **Function / Class** | `ft_seed_inventory(seed_type, quantity, unit)` |
| **Description** | Prints the seed inventory depending on the unit (`packets`, `grams`, `area`) |
| **Concepts** | Type hints, `if` / `elif` / `else`, f-strings, `str.capitalize()` |

</details>

### python_module_01 — Object-Oriented Garden Systems

<details>
<summary><b>ex0</b> — ft_garden_intro.py</summary>

| | |
|---|---|
| **Exercise** | `ex0` |
| **Directory** | `python_module_01/ex0/` |
| **File(s)** | `ft_garden_intro.py` |
| **Function / Class** | `presentation(name, height, age)` |
| **Description** | Displays a plant's information |
| **Concepts** | `if __name__ == "__main__":`, f-strings |

</details>

<details>
<summary><b>ex1</b> — ft_garden_data.py</summary>

| | |
|---|---|
| **Exercise** | `ex1` |
| **Directory** | `python_module_01/ex1/` |
| **File(s)** | `ft_garden_data.py` |
| **Function / Class** | `Plant` |
| **Description** | First `Plant` class with `name`, `height`, `age` and a `show()` method |
| **Concepts** | Classes, `__init__`, attributes, methods |

</details>

<details>
<summary><b>ex2</b> — ft_plant_growth.py</summary>

| | |
|---|---|
| **Exercise** | `ex2` |
| **Directory** | `python_module_01/ex2/` |
| **File(s)** | `ft_plant_growth.py` |
| **Function / Class** | `Plant` |
| **Description** | `grow()` (+0.8cm) and `age()` (+1 day) methods simulating one week of growth |
| **Concepts** | Changing an object's state through methods, `round()` |

</details>

<details>
<summary><b>ex3</b> — ft_plant_factory.py</summary>

| | |
|---|---|
| **Exercise** | `ex3` |
| **Directory** | `python_module_01/ex3/` |
| **File(s)** | `ft_plant_factory.py` |
| **Function / Class** | `Plant` |
| **Description** | Creates several `Plant` instances and displays each one |
| **Concepts** | Multiple instances of the same class |

</details>

<details>
<summary><b>ex4</b> — ft_garden_security.py</summary>

| | |
|---|---|
| **Exercise** | `ex4` |
| **Directory** | `python_module_01/ex4/` |
| **File(s)** | `ft_garden_security.py` |
| **Function / Class** | `Plant` |
| **Description** | Protected attributes (`_name`, `_height`, `_age`) with getters / setters rejecting negative values |
| **Concepts** | Encapsulation, getters / setters, data validation |

</details>

<details>
<summary><b>ex5</b> — ft_plant_types.py</summary>

| | |
|---|---|
| **Exercise** | `ex5` |
| **Directory** | `python_module_01/ex5/` |
| **File(s)** | `ft_plant_types.py` |
| **Function / Class** | `Plant`, `Flower`, `Tree`, `Vegetable` |
| **Description** | Plant subclasses with their own behaviour: `bloom()`, `produce_shade()`, `grow()` / `age()` |
| **Concepts** | Inheritance, `super()`, method overriding |

</details>

<details>
<summary><b>ex6</b> — ft_garden_analytics.py</summary>

| | |
|---|---|
| **Exercise** | `ex6` |
| **Directory** | `python_module_01/ex6/` |
| **File(s)** | `ft_garden_analytics.py` |
| **Function / Class** | `Plant`, `Plant.Stats`, `Flower`, `Seed`, `Tree`, `Vegetable` |
| **Description** | Nested `Stats` class counting `grow` / `age` / `show` / `shade` calls, `Seed` inheriting from `Flower`, `check_age()` and `create_anonymous()`, `show_stats()` working on any plant |
| **Concepts** | Nested classes, `@staticmethod`, `@classmethod`, multi-level inheritance, polymorphism |

</details>

### python_module_02 — Data Engineering for Smart Agriculture

## Resources

- [pyvision](https://www.github.com/ebayle42/pyvision/) by [ebayle42](https://www.github.com/ebayle42)
- [GeeksForGeeks (Functions)](https://www.geeksforgeeks.org/python/python-functions/)
- [GeeksForGeeks (Recursion)](https://www.geeksforgeeks.org/python/recursion-in-python/)
- [W3Schools (function range())](https://www.w3schools.com/python/ref_func_range.asp)
- [RealPython (if __name__ == "__main__")](https://realpython.com/if-name-main-python/)
- [IONOS (Class Python)](https://www.ionos.fr/digitalguide/sites-internet/developpement-web/classes-python/)
- [Docstring (Inheritance)](https://www.docstring.fr/glossaire/heritage/)
- [GeeksForGeeks (Static method)](https://www.geeksforgeeks.org/python/python-staticmethod/)
- [GeeksForGeeks (Class method)](https://www.geeksforgeeks.org/python/classmethod-in-python/)
- [GeeksForGeeks (str to int)](https://www.geeksforgeeks.org/python/convert-string-to-integer-in-python/)
- [W3Schools (ValueError)](https://www.w3schools.com/python/ref_exception_valueerror.asp)
- [GeeksforGeeks (Custom Errors)](https://www.geeksforgeeks.org/python/define-custom-exceptions-in-python/) 
- [Educative (__str__)](https://www.educative.io/answers/what-is-the-str-method-in-python)
- [GeeksForGeeks (sys-argv)](https://www.geeksforgeeks.org/python/how-to-use-sys-argv-in-python/)
- [GeeksForGeeks (Python lists)](https://www.geeksforgeeks.org/python/python-lists/)
- [GeeksForGeeks (sum() in Python)](https://www.geeksforgeeks.org/python/sum-function-python/)
- [GeeksForGeeks max() in Python](https://www.geeksforgeeks.org/python/python-max-function/)
- [GeeksForGeeks min() in Python](https://www.geeksforgeeks.org/python/python-min-function/)