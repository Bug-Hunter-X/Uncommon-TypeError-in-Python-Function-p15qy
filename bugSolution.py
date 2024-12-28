def function_with_uncommon_bug_solution(a, b):
    try:
        if not isinstance(a,(int, float)) or not isinstance(b,(int, float)):
            raise TypeError("Inputs must be numbers")
        result = a / b
        return result
    except ZeroDivisionError:
        return "Division by zero"
    except TypeError as e:
        return str(e)

#Demonstrating the solution
result = function_with_uncommon_bug_solution(10, "hello")
print(result)
result = function_with_uncommon_bug_solution(10, 0)
print(result)
result = function_with_uncommon_bug_solution(10, 2)
print(result)