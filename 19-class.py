# Scope

# globalS = "Global Variable"

# def ScopeFunc():
#     localS = "Local Variable"
    # print(globalS)
    # print(localS)
    # if 1 == 1:
    #     ifvar = "If Variable"
        # print(globalS)
        # print(localS)
        # print(ifvar)
        
    # print(globalS)
    # print(localS)
    # print(ifvar)
    
# print(globalS)
# print(localS)
# print(ifvar)
# ScopeFunc()

# class SampleClass:
#     a = 10
#     b = 20
    
# sa = SampleClass()
# print(sa.a)

# sb = SampleClass()
# print(sb.a)


class SampleClass:
    def __init__(self, h, w):
        self.a = h
        self.b = w
    a = 10
    b = 20
    def area(self):
        area = self.a * self.b
        return area
    def add(self, d, e):
        self.d = d
        self.e = e
        add = self.d + self.e
        return add
    
    
sa = SampleClass(23, 33)
# print(sa.area())
print(sa.add(2, 5))

sb = SampleClass(55, 65)
# print(sb.area())
print(sb.add(5, 6))






