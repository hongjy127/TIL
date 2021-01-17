class Date:
    def __init__(self,month):
        self.inner_month = month    # 밖에서 .inner_month로 접근하지 않음

    @property
    def month(self):                # month(property명)를 멤버변수처럼 사용 
        return self.inner_month

    @month.setter
    def month(self,month):
        if 1<=month<=12:
            self.inner_month = month


today = Date(8)
print(today)
today.month = 15
print(today.month)
today.month = 12
print(today.month)