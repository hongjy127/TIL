#include <iostream>
using namespace std;

int main(int argc, char const *argv[]){
    string str;

    do{
        cout << "���ڿ��� �Է��ϼ���:";
        // ���Ⱑ ��
        getline(cin, str);

        // ���Ⱑ �Ұ���
        // cin >> str;

        cout << "������� �Է�: " << str << endl;
    } while(str != "����");

    return 0;
}