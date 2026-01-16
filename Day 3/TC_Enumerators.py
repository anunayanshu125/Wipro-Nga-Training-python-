fruits=['apple','banana','orange','grapes']
for index,value in enumerate(fruits):
    print(index,value)

from enum import Enum
class color(Enum):
    Red=1
    Green=2
    Blue=3
    Yellow=4
print(color.Red.value)
print(color.Red.name)
print(color.Green.value)
print(color.Blue.value)