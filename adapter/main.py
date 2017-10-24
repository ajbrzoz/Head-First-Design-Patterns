class Duck:
    def quack(self):
        pass
    
    def fly(self):
        pass
    
    
class MallardDuck(Duck):
    def quack(self):
        print("Quack")
        
    def fly(self):
        print("I'm flying")
        
class Turkey:
    def gobble(self):
        pass
    
    def fly(self):
        pass


class WildTurkey(Turkey):
    def gobble(self):
        print("Gobble gobble")
    
    def fly(self):
        print("I'm flying a short distance")
        
        
class TurkeyAdapter(Duck):
    def __init__(self, turkey):
        self.turkey = turkey
        
    def quack(self):
        self.turkey.gobble()
        
    def fly(self):
        for i in range(5):
            self.turkey.fly()
            
            
class TurkeyClassAdapter(Duck, WildTurkey):
    def quack(self):
        WildTurkey.gobble(self)
        
    def fly(self):
        for i in range(5):
            WildTurkey.fly(self)
            

if __name__ == "__main__":
    duck = MallardDuck()
    turkey = WildTurkey()
    turkey_adapter = TurkeyAdapter(turkey)
    turkey_class_adapter = TurkeyClassAdapter()
    
    print("The Turkey says...")
    turkey.gobble()
    turkey.fly()
    
    print("The Duck says...")
    duck.quack()
    duck.fly()

    print("The TurkeyAdapter says...")
    turkey_adapter.quack()
    turkey_adapter.fly()

    print("The TurkeyClassAdapter says...")
    turkey_class_adapter.quack()
    turkey_class_adapter.fly()