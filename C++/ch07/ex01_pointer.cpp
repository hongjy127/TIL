#include <iostream>
using namespace std;

int main(){
    int number = 0;
    int *p = &number;

    cout << p << endl;
    cout << *p << endl;
    cout << sizeof(p) << endl;

    return 0;
}