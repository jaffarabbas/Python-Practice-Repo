from multiprocessing import Process

def loop_a():

     for i in range(0,10):

        print("first")

def loop_b():

    for i in range(0,10):

        print("secon")

if __name__ == '__main__':

    Process(target=loop_a).start()

    Process(target=loop_b).start()