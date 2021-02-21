#include <iostream>
using namespace std;

int main() {
    int sum = 0;
    // i는 for문 안에서만 쓰이는 지역변수
    for(int i=0; i<=10; i++) {
        sum += i;
    }

    cout << "1부터 10까지 정수의 합 = " << sum << endl;
    return 0;
}