class Error(Exception):
    pass

class ConvertError(Error):
    def __init__(self, unit1, unit2) -> None:
        super().__init__(f'Cannot convert from {unit1} to {unit2}')

class UnitError(Error):
    def __init__(self, unit) -> None:
        super().__init__(f"Unidentified symbol: {unit!r}")

class OperatorError(Error):
    pass

class ExcessOpError(OperatorError):
    def __init__(self) -> None:
        super().__init__("Excess operator")

class MissingOpError(OperatorError):
    def __init__(self):
        super().__init__("Missing operator")

class NumberError(Error):
    def __init__(self):
        super().__init__("Incorrect number format")

class BracketError(Error):
    def __init__(self):
        super().__init__("Missing bracket")

class OperandError(Error):
    def __init__(self):
        super().__init__("Missing operand")

class EmptyError(Error):
    def __init__(self):
        super().__init__("Empty expression")

class DivisionError(Error):
    def __init__(self):
        super().__init__("Division by zero")
        
class TemperatureError(Error):
    def __init__(self):
        super().__init__("Temperature below zero is not allowed")