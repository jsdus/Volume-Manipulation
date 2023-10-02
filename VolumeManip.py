    ###########################################################
    #
    #  Computer Project #11
    #
    #  Develop a program class that allows a user to manipulate volume measurements.
    #    Program will consist of methods.
    #
    #   __init__:
    #    initializes parameters for the class and erro checks.
    #
    #   __repr__ and __str__:
    #    returns a representation of the current object as a character string.
    #       repr has 6 decimals and str has 3.
    #
    #   .is_valid :
    #    Returns a boolean to indicate whether or not object is valid.
    #
    #   .get_units:
    #    Returns units stored during construction.
    #   
    #   .get_magnitude:
    #    Returns magnitude stored during construction.
    #
    #   .metric:
    #    Returns volume object equivalent to object.
    #
    #   .customary:
    #    Returns a volume object equivalent to object.
    #
    #   __eq__:
    #    Compares the magnitude of two volume objects.
    #
    #   .add & .sub:
    #    Sum/difference computed based on magnitude of two objects, units converted if objects are in different systems.
    #
    ###########################################################

UNITS = ["ml","oz"]
MLperOZ = 29.5735295625  # ml per oz
DELTA = 0.000001

class Volume(object):
    def __init__(self, magnitude = 0 , units = 'ml'):   #constructor for magnitude and units
        '''
        Constructor to define magnitude and units, makes sure volume has a valid magnitude and units.
        magnitude: user specified magnitude (int/float)
        units: user specified units (str)
        '''
        try: # try and except to catch error 
            if magnitude.isdigit() == False : # if magnitude is not a number, magnitude and units = None
                self.magnitude = None
                self.units = None
        except AttributeError:
            
            if magnitude >= 0 and units in UNITS: # if magnitude is greater than zero and has valid units, set.
                self.magnitude = magnitude
                self.units = units
            
            if units not in UNITS: # if unit given is not valid, set magnitude and units to None
                self.units = None
                self.magnitude = None
            if magnitude < 0: # if magnitude is negative, set magnitude to 0 and units to None
                self.magnitude = 0
                self.units = None
    
        
    def __str__(self):    
        '''
        Representation of current object as a string to 3 decimals.
        Returns: string of object (str)
        '''
        if self.units == None or self.magnitude == None: # if object is invalid, return string invalid
            invalid = 'Not a Volume'
            return invalid
        
        else:
            valid = '{:.3f} {}'.format(self.magnitude,self.units) # if object is valid, return formatted string
            return valid

        
    def __repr__(self):    
        '''
        Diplays magnitude rounded to six decimals.
        Returns: formatted string of object(str)
        '''
        if self.units == None or self.magnitude == None: # if object is invalid, print not a volume
            invalid = 'Not a Volume'
            return invalid
        
        else:
            valid = '{:.6f} {}'.format(self.magnitude,self.units) # if valid, return formatted string
            return valid

        
    def is_valid(self):    
        '''
        Indicates whether is valid or not.
        Returns: boolean indicating validity (bool)
        '''
        if self.units == None or self.magnitude == None: # if object is invalid, return False
            validity = False
            return validity
        else:
            validity = True # else True
            return validity

    
    def get_units(self):     
        '''
        Units of object during construction.
        Returns: returns unit if valid (str) and None otherwise.
        '''
        if self.is_valid() == True: # if object is valid return unit
            return self.units
        
        else:
            return None
        
    def get_magnitude(self):  
        '''
        Magnitude of object during construction
        Returns: returns magnitude (int) of object if valid and None otherwise.
        '''
        if self.magnitude != None: # if magnitude does not equal none, return magnitude
            return self.magnitude
        
        else:
            return None

    
    def metric(self):      
        '''
        Returns a volume object equivalent to original object.
        Returns: new object (volume)
        '''
        if self.is_valid() == True: # if object is valid, check units and convert magnitude to make new object.
            if self.units == 'ml':
                return Volume(self.magnitude,self.units)
            if self.units == 'oz':
                new_mag = self.magnitude * MLperOZ
                return Volume(new_mag, 'ml')
        else: # else return the invalid object as new
            return Volume(self.magnitude,self.units)

    def customary(self): 
        '''
        Returns a volume object equivalent to original object.
        Returns: new object (volume)
        '''
        if self.is_valid() == True:  # if object is valid, check units and convert magnitude to make new object.
            if self.units == 'oz':
                return Volume(self.magnitude,self.units)
            if self.units == 'ml':
                new_mag = self.magnitude / MLperOZ
                return Volume(new_mag, 'oz')
        else:
            return Volume(self.magnitude,self.units)
        
    def __eq__(self,other): 
        '''
        Compares magnitude of two volume objects, converts units if the units are not the same.
        other: second volume object (volume)
        Returns: boolean value if two magnitudes are of equal value. (bool)
        '''
        x = self.metric() # convert both to the same unit
        y = other.metric()
        if y.is_valid() == False or x.is_valid() == False: # if either of original are invalid just return False
            return False
        else:
            return (abs(y.get_magnitude() - x.get_magnitude()) < DELTA) # else return if they are equal.

    
    
    
    def add(self,other):  
        '''
        Computes the sum of two volume objects.
        other: second volume object(volume)
        Returns: new volume object. (volume)
        
        '''
        unit = self.get_units() # get unit of left hand object to make sure  all objects are the same units
        try:
            if self.is_valid() == False or other.is_valid() == False:
                return False
            
            if unit == 'ml':
                converted = other.metric() #convert second object to metric
                summ = self.get_magnitude() + converted.get_magnitude()
                return Volume(summ,'ml')
            if unit == 'oz':
                converted = other.customary() #convert second object to customary
                summ = self.get_magnitude() + converted.get_magnitude()
                return Volume(summ,'oz')
            
        except AttributeError:
            if unit == 'ml':
                summ = self.get_magnitude() + other
                return Volume(summ,'ml')
            if unit == 'oz':
                summ = self.get_magnitude() + other
                return Volume(summ,'oz')
    
    def sub(self,other): 
        '''
        Computes the difference of two volume objects.
        other: second volume object(volume)
        Returns: new volume object. (volume)
        '''
        unit = self.get_units() # get unit of left hand object to make sure  all objects are the same units
        try:
            if self.is_valid() == False or other.is_valid() == False:
                return False
            
            if unit == 'ml':
                converted = other.metric() #convert second object to metric
                diff = self.get_magnitude() - converted.get_magnitude()
                return Volume(diff,'ml')
            if unit == 'oz':
                converted = other.customary() #convert second object to customary
                diff = self.get_magnitude() - converted.get_magnitude()
                return Volume(diff,'oz')
        except AttributeError:
            if unit == 'ml':
                summ = self.get_magnitude() - other
                return Volume(summ,'ml')
            if unit == 'oz':
                summ = self.get_magnitude() - other
                return Volume(summ,'oz')