#include<iostream>
using namespace std;

// const를 하면 warning 사라짐
void print(const char *str){  // 아두이노 라이브러리...
    cout << str << endl;
}

void print2(string str){
    cout << str << endl;
}

// 문자열을 나타내는 3가지 방법
int main(){
    char **p;   // 이중 포인터  **********p 개수제한 없이 가능


    // 캐릭터 포인터
    char *str1 = "Hello";   // new, delete
    // 문자 배열
    char str2[10] = "Hello"; // memory 문제
    // string 객체 이용
    string str3 = "Hello"; // 다 되지만 print(char)를 못 넘김...

    cout << str1 << endl;
    cout << str2 << endl;
    cout << str3 << endl;

    // 문법적으로는 맞지만 상수이므로 불가능함
    // str1[2] = 'L';  // *(str1+2) = L --> HeLlo
    // warning: ISO C++ forbids converting a string constant to 'char*'-Wwrite-strings]
    // 그래서 이런 warning 발생(문법적으로 걸러줄 수 없음)

    str2[2] = 'L';
    cout << str2 << endl;

    print(str1);    // ok
    print(str2);    // ok, 배열명 -> 배열의 시작 주소... char *
    // print(str2[0]);
    print(&str2[0]);    // char *
    print(&str2[1]);    // char *
    // print(str3); // 타입이 맞지 않음
    // print(&str3); // string의 주소가 되므로 not ok

    print2(str1);   // string str = "Hello" --> ok
    print2(str2);   // string str = "Hello" --> ok
    print2(str3);   // ok

    // 아두이노 --> str3.c_str()

    print("World"); // char *str = "World"


    return 0;
}
