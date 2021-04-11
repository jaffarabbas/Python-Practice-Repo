#quiz app 

count = 0

quetsion = {
    1 : {
        'q': 'what is your name ?',
        'option' : ["jaffar" , "imad" , "aliyan"],
        'answer' : 'jaffar' 
    },
    2 : {
        'q': 'what is your car name ?',
        'option' : ["lamborgini" , "farari" , "car"],
        'answer' : 'car' 
    },
    3 : {
        'q': 'what is your age ?',
        'option' : ["21" , "22" , "24"],
        'answer' : '24' 
    }
}


for i in quetsion:
    print("Question :",i)
    print(quetsion[i]['q'])

    print(quetsion[i]['option'])
    a = input("Your answer : ")
    if(a == quetsion[i]['answer']):
        print("YEs")
        count += 1
    else:
        print("No")

if(count>=3):
    print("Won")
else:
    print("Loss")
