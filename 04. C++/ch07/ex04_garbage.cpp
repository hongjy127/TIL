#include <iostream>
#include <time.h>
using namespace std;

int main(){
    int *ptr = new int;

    *ptr = 99;
    delete ptr;

    return 0;
}