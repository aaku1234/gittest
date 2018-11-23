class complex:
    def __init__(self,realpart,imagpart):
        self.r= realpart
        self.i= imagpart
    def f(self):
        return "hello"
x= complex(3.0,-4)
print(x.r)
print(x.i)
print(x.f())
#class function for attribute
print(hasattr(x,'r'))
print(getattr(x,'r'))
print(setattr(x,'r',6.0))
print(x.r)
print(delattr(x,'r'))
