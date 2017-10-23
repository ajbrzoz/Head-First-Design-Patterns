class ChocolateBoiler:
    empty = True
    boiled = False
    unique_instance = None
    
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not cls.unique_instance:
            cls.unique_instance = super(ChocolateBoiler, cls).__new__(*args, **kwargs)
        return cls.unique_instance
    
    def fill(self):
        if self.empty:
            self.empty = False
            self.boiled = False
            
    def drain(self):
        if not self.empty and self.boiled:
            self.empty = True
    
    def boil(self):
        if not self.empty and not self.boiled:
            self.boiled = True
