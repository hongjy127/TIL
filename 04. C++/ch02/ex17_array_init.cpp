#include <iostream>
using namespace std;

int main() {
    int score[] = {
        100, 200, 300, 400, 502
    };

    const int STUDENTS = sizeof(score)/sizeof(int);

    int sum = 0;
    int i;
    double average;

    for(i=0; i<STUDENTS; i++) {
        sum += score[i];
    }

    // datatype이 다른 경우 표현범위가 큰쪽으로 바뀜
    average = (double)sum/STUDENTS; // (): 캐스팅 연산자
    cout << "성적 평균 " << average << endl;

    return 0;
}