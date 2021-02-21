#include<iostream>
#include<string>
using namespace std;

class Shape{
protected:
    int x, y;
public:
    void draw() {
        cout << x << "," << y << endl;
    }
    void move() {}
};

class Rectangle: public Shape{
protected:
    int width;
    int height;
public:
    int calcArea(){
        cout << x << "," << y << endl; // 자식 접근 가능
        return width*height;
    }
};

int main(){
    Rectangle r;
    // r.x = 10;       // protected - error
    // r.width = 200;  // protected - error

    r.calcArea();
    r.move();

    return 0;
}