
class Vehicle:
    '''
    Vehicle Class
    This class models a vehicle on a used car lot
    Change order: we need to add maximum speed to the model
    Change order: need a way to 'read' maximum speed
    Change order: some developers need to use the constructor without having a max speed
    '''
    def __init__(self, type, max_speed= None):
        self.type = type;
        self._thisisprivate = 42 #This is a weak attempt to 'support' data hiding
        self.max_speed = max_speed
        '''
        @param type: The kind of vehicle on lot
        @param: max_speed: Maximum speed of the vehicle. Defaults to none
        '''
        
    def printType(self):
        print(self.type);
    def getSpeed(self):
        return self.max_speed # a getter 
if __name__ == "__main__":
# Some code to test the class would go here.
# If there's no code, just pass
    pass