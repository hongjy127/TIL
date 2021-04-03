#include <iostream>
using namespace std;

int main() {
    const int STUDENTS = 3;

    int score[STUDENTS];
    int sum = 0;
    int i;
    int average;
    // double average;

    for(i=0; i<STUDENTS; i++) {
        cout << "학생들의 성적을 입력하시오: ";
        cin >> score[i];
    }

    for(i=0; i<STUDENTS; i++) {
        sum += score[i];
    }

    average = sum / STUDENTS;
    cout << "성적 평균 = " << average << endl;
    return 0;
}