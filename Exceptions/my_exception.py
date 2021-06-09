class NotAllEven(Exception):
    def __init__(self, arr) -> None:
        self.flag = False
        self.arr = []
        for el in arr:
            if el % 2:
                super().__init__("Not all elements in the list are even!")
                self.arr.append(el)
                self.flag = True

    
try:
    q = NotAllEven([2,6,4,22,0])
    if q.flag:
        raise q
except NotAllEven as nae:
    print("Not even elements are: {}".format(nae.arr))
else:
    print("All elements are even.")
finally:
    print("Try-except block is passed.")