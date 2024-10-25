Here is a simple Python code for a random number generator that prints "Your lucky number is [random number]".

```python
import random

def lucky_number():
    number = random.randint(1, 100)
    print("Your lucky number is", number)

lucky_number()
```