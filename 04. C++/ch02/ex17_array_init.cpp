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

    // datatype�� �ٸ� ��� ǥ�������� ū������ �ٲ�
    average = (double)sum/STUDENTS; // (): ĳ���� ������
    cout << "���� ��� " << average << endl;

    return 0;
}