#guess the number game
import random

class game:
     count = 0
     mincount = 5
     score = 10
     finalscore = 0
     
     def genrateNumber(self,start,end):
         return random.randint(start,end)
    
     def Guesser(self):
        while True:
            if(self.count != 3):
                while True:
                    print("GUSESS NUMBER")
                    number = int(input('Guess Number : '))
                    
                    ran = self.genrateNumber(0,10)
                    
                    if(number == ran):
                        print(ran," is the guess number won !!!" , self.mincount , self.count)
                        self.finalscore += self.score
                        break
                    else:
                        self.mincount -= 1
                        if self.mincount == -1:
                            print("Faild ")
                            break
                        else:
                            print("Wrong !! count left : " , self.mincount , "Current level : ",self.count) 
                                
                self.count += 1           
            else:
                print("Score : ",self.finalscore)
                break

def main():
    ob = game()
    ran =  ob.genrateNumber(0,10)
    print(ran)
    ob.Guesser()


if __name__ == '__main__':
    main()
    