#include <iostream>
#include <string>
using namespace std;

class Circle{
    public:
    // 인스턴스 멤버 초기화: 생성자(python: __init__)
    // 초기화 안함, 공간은 확보하되 임의의 값이 들어감.
    int radius;
    string color;

    double calcArea(){
        return 3.14*radius*radius;
    }
};

void print(Circle p){
    cout << "Area " << p.calcArea() << endl;
}

int main(){
    Circle pizza1, pizza2;

    // 여기서 초기화
    pizza1.radius = 100;
    pizza1.color = "yellow";
    // cout << "Area " << pizza1.calcArea() << endl;

    print(pizza1);  // p=pizza1; call by value

    pizza2.radius = 200;
    pizza2.color = "white";
    // cout << "Area " << pizza2.calcArea() << endl;
    print(pizza2);

    // pizza1을 복사함.
    Circle pizza3 = pizza1;
    print(pizza3);

    return 0;
}