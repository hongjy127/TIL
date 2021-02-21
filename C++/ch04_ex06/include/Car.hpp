#pragma once

#include <string>
using namespace std;

// Car 클래스의 signature(원형)
class Car {
protected:
    int speed;
    int gear;
    string color;

public:
    int getSpeed();
    void setSpeed(int s);
};