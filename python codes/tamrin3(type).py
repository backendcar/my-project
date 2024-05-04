def test_method(self):
    print("This is Test class method!")

# creating a base class
class Base:
    def myfunc(self):
        print("This is inherited method!")

# creating Test class dinamically using 
# type() method directly
Test = type('Test',(Base, ),dict(x="atul",my_method=test_method))

print("Type of Test class: ", type(Test))

# creating instance of Test class
test_obj = Test()
print("Type of test_obj: ", type(test_obj))

# calling inherited method
test_obj.myfunc() # class Base in line 4

# calling Test class method
test_obj.my_method() 

# printing variable
print(test_obj.x)
