
class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: Does not need to access class or instance data
    @staticmethod
    def add(a, b):
        return a + b

    # Class method: Can access class-level data (such as class attributes)
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
