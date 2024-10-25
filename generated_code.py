Sure, here is a simple example of a random number generator in Python using the built-in `random` module:

```python
import random

def random_number_generator(min_val=1, max_val=100):
    return random.randint(min_val, max_val)

# Generate a random number between 1 and 100
print(random_number_generator())
```

In this code, the `random_number_generator` function generates a random integer between `min_val` and `max_val` (both inclusive). By default, it generates a number between 1 and 100, but you can specify different boundaries by passing arguments to the function. For example, `random_number_generator(200, 300)` will generate a random number between 200 and 300.