class Date:
    def __init__(self, month):
        self.__month = month

    def getmonth(self):
        return self.__month

    def setmonth(self,month):
        if 1<=month<=12:
            self.__month = month

    month = property(getmonth, setmonth)

today = Date(8)
print(today)
today.month = 15
print(today.month)
today.month = 12
print(today.month)