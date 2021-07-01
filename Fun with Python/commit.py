  
import os
import random
import string


count = 0
while count == 0:
    import random
    n = random.randint(10,20)
    n = 10 # 1 Mb of text
    chars = ''.join([random.choice(string.letters) for i in range(n)])
    with open('textfile.txt', 'w+') as f:
        f.write(chars)
    os.system("git add .")
    os.system("git commit -m 'Unlimited Commit'")
    os.system("rm textfile.txt")