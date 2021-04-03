#include <iostream>
#include <string>
using namespace std;

int main(){
    string s="When in Rome, do as the Romans.";

    int size = s.size();
    int index = s.find("Rome");

    cout << size << endl;
    cout << index << endl;

    for(auto& ch:s){
        cout << ch << ' ';
    }

    return 0;
}