Here's a simple Python script that wishes the user a happy birthday:

```python
# Python script to wish user a Happy Birthday

def birthday_wish(name):
    print("Happy Birthday, {}!".format(name))

name = input("Please enter your name: ")
birthday_wish(name)
```

In this script, we define a function called `birthday_wish()` that takes a name as an argument and prints a birthday message for that name. We then ask the user to enter their name, and call the `birthday_wish()` function with the name the user entered.