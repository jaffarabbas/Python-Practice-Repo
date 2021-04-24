import sys
import operator

class calculater:
    
    def __init__(self,num,num2):
        self.num = num
        self.num2 = num2
        
    def add(self):
        return self.num + self.num2
    def sub(self):
        return self.num - self.num2
    def mul(self):
        return self.num * self.num2
    def divi(self):
        return self.num / self.num2
    
    def machine(self,prefix,calculater):      
            if(prefix == '+'):
                print(calculater.add())
            elif(prefix == '-'):
                print(calculater.sub())
            elif (prefix == '*'):
                print(calculater.mul())
            elif (prefix == '/'):
                print(calculater.div())
            else:
                print("No Operater")

def main():
   try:
        while True:
            num1  = int(input("Enter Number 1 : "))
            num2  = int(input("Enter Number 2 : "))
                
            cal  = calculater(num1,num2)
            prefixes =  input("Enter Character : ")
            cal.machine(prefixes,cal)
        
            if prefixes == 'o':
                break
   except:
       print(sys.exc_info())
        
if __name__ == '__main__':
    main()
    