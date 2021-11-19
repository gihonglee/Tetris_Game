a = []
class dummy:
    def __init__(self,a):
        self.main = 1
        self.a = a

    def update_a(self,input):
        self.a.append(input)

b = dummy(a)
b.update_a(1)
print(a)
print(b.a)

