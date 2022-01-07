class ClassTest:
    
    def instance_method(self):
        print(f"Called instance_method of {self}")
        
test = ClassTest()
test.instance_method()
ClassTest.instance_method(test)