from bs4 import BeautifulSoup

with open('ezine_02_template_1218/index.html','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content,'lxml')
    tags = soup.find_all('h2')
    class_wrapper = soup.find_all('div',id="contentwrapper")
    for i in class_wrapper:
        print(type(i.h2.text))
        print(i.h2.text,'\n')
        print(i.a.text, '\n')
        spliterh2 = i.h2.text.split()
        print(spliterh2)
        #searaching lorial
        for i in spliterh2:
            if(i == 'consectetuer'):
                print(i)
                break


