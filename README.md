Develop a program class that allows a user to manipulate volume measurements.

Program will consist of methods.
__init__:
initializes parameters for the class and erro checks.

__repr__ and __str__:
returns a representation of the current object as a character string.
repr has 6 decimals and str has 3.

.is_valid :
Returns a boolean to indicate whether or not object is valid.

.get_units:
Returns units stored during construction.

.get_magnitude:
Returns magnitude stored during construction.

.metric:
Returns volume object equivalent to object.

.customary:
Returns a volume object equivalent to object.

__eq__:
Compares the magnitude of two volume objects.

.add & .sub:
Sum/difference computed based on magnitude of two objects, units converted if objects are in different systems.
