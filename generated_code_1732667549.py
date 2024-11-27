Sure, here is a simple Python program that finds the factorial of a number.

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

num = 5
print("The factorial of", num, "is", factorial(num))
```