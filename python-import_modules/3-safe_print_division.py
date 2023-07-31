def safe_print_division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Division by zero is not allowed.")
        return None
    except Exception as e:
        print("Unexpected error occurred:", e)
        return None
    finally:
        print("Inside result: {}".format(result))
        return result

# Example usage:
a = 10
b = 2
safe_print_division(a, b)
