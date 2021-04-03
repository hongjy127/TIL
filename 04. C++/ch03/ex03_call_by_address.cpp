#include <iostream>
using namespace std;

// call by address
// 주소를 받는 것이므로 크기를 정해주면 안됨 int arr[]
int test(int arr[]){
    int s = sizeof(arr);    // 주소의 크기(항상 8byte)
    cout << "array size : " << s << endl;
    arr[0] = 10;    // arr가 받은 주소의 0번쨰 index
    return arr[0];
}

int main(int argc, char const *argv[]) {
    int n[] = {1,2,3,4,5};
    cout << "array n size : " << sizeof(n) << endl;
    int m = test(n); // 배열 이름: 배열의 시작 주소를 넘김

    cout << "result : " << n[0] << endl;
    return 0;
}