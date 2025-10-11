# class_static_methods_demo.py

class Calculator:
    # Class attribute (shared by all instances and accessible by class methods)
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method — does not depend on any class or instance data.
        You can call this directly using the class name: Calculator.add(10, 5)
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method — uses 'cls' to access the class attribute.
        Here, it prints the calculation_type before performing multiplication.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
