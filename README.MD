# Sea trading

## Python OOP
- class
- object (instacja klasy)
- self (referencja do obiektu)
- method (funkcja w kontekscie klasy)
  - default (self)
  - staticmethod ()
  - classmethod (cls)
- field/attribiutes
  - object field (self)
  - class field 
- python features (magic methods)
  - `__str__` -> string
  - `__len__` -> int
  - `__repr__` -> string
  - `__format__` -> string
  - `__name__` -> string
  - `__init__` -> None
  - `__new__` -> self/(?object)
- constructor
- object descriptor/data object descriptor (getter/setter/deleter)
- property - class data object descriptor protocol
- super 
- MRO - method resolution order (C3)

## OOP Rules
1. Abstraction
2. Inheritance
3. Polymorphism
4. Encapsulation
   - private
   - protected
   - public
   - read_only

## SOLID
1. Single responsibility
2. Open/closed principle
3. Liskov Substitution principle
4. Interface segregation principle 
5. Dependency inversion 

## Hierarchy
- Interface - requirements, no implementation detail
- Abstract Class - requirements, partially implenentation detail
- Concrete Class - implementation detail

---

- metaclass
- class
- object

## Examples:

```python

class X:
    b = 'on class'
    
    def __init__(self):
        self.a = 'on instance'
        print(X.b)
        self.a = 're-bound'
        self.b = 'new on instance'
        print(self.b)
        print(self.a)


```