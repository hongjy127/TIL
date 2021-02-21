#include<iostream>
#include<string>
using namespace std;

class printData{
    public:
    void print(int i) {cout << i << endl;}
    void print(double f) {cout << f << endl;}
    void print(string s = "No Data!") {cout << s << endl;}
};

int main(){
    printData prn;

    prn.print(1);
    prn.print(3.14);
    prn.print("C++ is cool.");
    prn.print();

    return 0;
}