import time
from timeit import default_timer as timer

def main():
    while True:
        x = input("para parar 1")
        if x==1:
            start = timer()
        if x==0:
            end = timer()
            print(end - start)
        time.sleep(3)

if __name__ == '__main__':
    main()
