#include<iostream>
#include<string>
using namespace std;

class Shape{
    int x,y;
public:
    Shape(){
        cout << "Shape()" << endl;
    }

    Shape(int xloc, int yloc): x(xloc), y(yloc){
        cout << "Shape(xloc, yloc)" << endl;
    }

    ~Shape(){
        cout << "~Shape()" << endl;
    }
};

class Rectangle: public Shape{
    int width, height;
public:
    Rectangle(){
        cout << "Rectangle()" << endl;
    }

    Rectangle(int x, int y, int w, int h):Shape(x,y), width(w), height(h){
        cout << "Rectangle(x,y,w,h)" << endl;
    }

    ~Rectangle(){
        cout << "~Rectangle()" << endl;
    }
};

int main(int argc, char const *argv[]){
    Rectangle r1;
    cout << endl;
    Rectangle r2(0,0,100,100);
    cout << endl;

    return 0;
}