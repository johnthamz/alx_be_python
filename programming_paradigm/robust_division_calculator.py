# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert inputs to float (this may raise ValueError if not numeric)
        num = float(numerator)
        den = float(denominator)

        # Perform division (this may raise ZeroDivisionError if den == 0)
        result = num / den
        return f"The result of the division is {result}"
    
    except ValueError:
        return "Error: Please enter numeric values only."
    
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
