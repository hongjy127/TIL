#include <iostream>
using namespace std;

int main() {
    int list[] = {1,2,3,4,5};

    for(int i : list) {
        i += 10;
    }
    for(int i : list) {
        cout << i << endl;
    }

    for(auto& i : list ) {
        i += 10;
    }
    for(int i : list) {
        cout << i << endl;
    }
    
    return 0;
}