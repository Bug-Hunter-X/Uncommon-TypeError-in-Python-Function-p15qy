def function_with_uncommon_bug(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError:
        return "Invalid input type"

# The following demonstrates the uncommon TypeError 
result = function_with_uncommon_bug(10, "hello")
print(result)