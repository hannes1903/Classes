
class MyCounter(dict):

    def __init__(self, l):
        super().__init__()
        for item in l:
            if item in self:
                self[item] += 1
            else:
                self[item] = 1

    def most_common(self):
        m = None
        for k, v in self.items():
            if m is None:
                m = (k, v)
            else:
                if v > m[1]:
                    m = (k, v)
        return m

    @classmethod
    def foo(cls):  #class
        print ("hello")


def main():
    a = [1,2,3,1,2,1,1,1,4]
    c= MyCounter(a)  #instance
    print(c)
    print (c.most_common())
    print(1 in c)
    print(c[1])
    MyCounter.foo()


if __name__ =="__main__":
    main()