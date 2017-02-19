# Effective Python

*59 Specific Ways to Write Better Python*<br>
by [Brett Slatkin](http://www.onebigfluke.com/), Senior Staff Software Engineer @ Google

- [Official site](http://www.effectivepython.com/)
- [Source code](https://github.com/bslatkin/effectivepython)
- [Errata](https://github.com/bslatkin/effectivepython/blob/master/Errata.md)
- Safari Books Online
  - [Book (March 2015)](https://www.safaribooksonline.com/library/view/effective-python-59/9780134034416/)
  - [Video (August 2015)](https://www.safaribooksonline.com/library/view/effective-python/9780134175249/)

---

## Preface

- Audience: Advanced programmers who want to be more effective in Python (i.e., being more Pythonic)
- Examples use Python 3 by default

## Acknowledgements

## About the Author

## 1. Pythonic Thinking

### 1. Know Which Version of Python You're Using

### 2. Follow the PEP 8 Style Guide

### 3. Know the Differences Between `bytes`, `str`, and `unicode`

### 4. Write Helper Functions Instead of Complex Expressions

### 5. Know How to Slice Sequences

### 6. Avoid Using `start`, `end`, and `stride` in a Single Slice

### 7. Use List Comprehensions Instead of `map` and `filter`

### 8. Avoid More Than Two Expressions in List Comprehensions

### 9. Consider Generator Expressions for Large Comprehensions

### 10. Prefer `enumerate` Over `range`

### 11. Use `zip` to Process Iterators in Parallel

### 12. Avoid `else` Blocks After `for` and `while` Loops

### 13. Take Advantage of Each Block `try`/`except`/`else`/`finally`

## 2. Functions

### 14. Prefer Exceptions to Returning None

### 15. Know How Closures Interact with Variable Scope

### 16. Consider Generators Instead of Returning Lists

### 17. Be Defensive When Iterating Over Arguments

### 18. Reduce Visual Noise with Variable Positional Arguments

### 19. Provide Optional Behavior with Keyword Arguments

### 20. Use `None` and Docstrings to Specify Dynamic Default Arguments

### 21. Enforce Clarity with Keyword-Only Arguments

## 3. Classes and Inheritance

### 22. Prefer Helper Classes Over Bookkeeping with Dictionaries and Tuples

### 23. Accept Functions for Simple Interfaces Instead of Classes

### 24. Use `@classmethod` Polymorphism to Construct Objects Generically

### 25. Initialize Parent Classes with `super`

### 26. Use Multiple Inheritance Only for Mix-in Utility Classes

### 27. Prefer Public Attributes Over Private Ones

### 28. Inherit from `collections.abc` for Custom Container Types

## 4. Metaclasses and Attributes

### 29. Use Plain Attributes Instead of Get and Set Methods

### 30. Consider `@property` Instead of Refactoring Attributes

### 31. Use Descriptors for Reusable `@property` Methods

### 32. Use `__getattr__`, `__getattribute__`, and `__setattr__` for Lazy Attributes

### 33. Validate Subclasses with Metaclasses

### 34. Register Class Existence with Metaclasses

### 35. Annotate Class Attributes with Metaclasses

## 5. Concurrency and Parallelism

### 36. Use subprocess to Manage Child Processes

### 37. Use Threads for Blocking I/O, Avoid for Parallelism

### 38. Use Lock to Prevent Data Races in Threads

### 39. Use Queue to Coordinate Work Between Threads

### 40. Consider Coroutines to Run Many Functions Concurrently

### 41. Consider `concurrent.futures` for True Parallelism

## 6. Built-in Modules

### 42. Define Function Decorators with `functools.wraps`

### 43. Consider `contextlib` and with Statements for Reusable `try`/`finally` Behavior

### 44. Make `pickle` Reliable with `copyreg`

### 45. Use `datetime` Instead of `time` for Local Clocks

### 46. Use Built-in Algorithms and Data Structures

### 47. Use `decimal` When Precision Is Paramount

### 48. Know Where to Find Community-Built Modules

## 7. Collaboration

### 49. Write Docstrings for Every Function, Class, and Module

### 50. Use Packages to Organize Modules and Provide Stable APIs

### 51. Define a Root Exception to Insulate Callers from APIs

### 52. Know How to Break Circular Dependencies

### 53. Use Virtual Environments for Isolated and Reproducible Dependencies

## 8. Production

### 54. Consider Module-Scoped Code to Configure Deployment Environments

### 55. Use `repr` String for Debugging Output

### 56. Test Everything with `unittest`

### 57. Consider Interactive Debugging with `pdb`

### 58. Profile Before Optimizing

### 59. Use `tracemalloc` to Understand Memory Usage and Leaks
