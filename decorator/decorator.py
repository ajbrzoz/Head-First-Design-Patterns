class Beverage:
    def __init__(self):
        self.description = "Unknown Beverage"
        
    def get_description(self):
        return self.description
    
    def cost(self):
        raise NotImplementedError
    
    
        