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
        cout << "�л����� ������ �Է��Ͻÿ�: ";
        cin >> score[i];
    }

    for(i=0; i<STUDENTS; i++) {
        sum += score[i];
    }

    average = sum / STUDENTS;
    cout << "���� ��� = " << average << endl;
    return 0;
}