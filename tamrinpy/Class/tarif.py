# کلاس ماشین
class Car:
    def __init__(self,model,color): # متدی برای شناساندن ویژگی های ماشین به کلاس 
        self.model = model    #شناساندن مدل ماشین 
        self.color = color    #شناساندن رنگ 
        
    def move(self):
        print(f"Car {self.model}")
        
    pride = Car("red", "Toyota")
    
   
    
    