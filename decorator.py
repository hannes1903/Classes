import time

def timer (add=0):

    def decor(fun):
        def internal(n1, n2):
            t = time.time()
            res = fun(n1, n2) + add
            print(time.time() - t)
            return res

        return internal

    return decor

@timer (add=5)
def add(a, b):
    time.sleep(5)
    return a+b

def main():
    print (add(1, 2))

if __name__ =="__main__":
    main()