"""
from Car_class import Car, ElectricCar

my_beetle = Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())
"""

from Ch9 import ClassCar

my_beetle = ClassCar.Car('volkswagen', 'beetle', 2016)
print(my_beetle.get_descriptive_name())

my_tesla = ClassCar.ElectricCar('tesla', 'roadster', 2016)
print(my_tesla.get_descriptive_name())