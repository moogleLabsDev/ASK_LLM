from enum import Enum

class Color(Enum):
  RED = 1
  GREEN = 2
  BLUE = 3

# Accessing enum members
print(Color.RED)
print(Color.RED.value)

# Iterating over enum members
for color in Color:
  print(color.name, color.value)