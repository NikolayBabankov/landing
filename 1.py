class IncrementCounter:
    
    def __init__(self):
        self._value = 0
    
    def new_value(self):
        self._value += 1
        return self._value


counter1 = IncrementCounter()

print(counter1.new_value())
print(counter1.new_value())
print(counter1.new_value())
x = counter1.print()
print(x)