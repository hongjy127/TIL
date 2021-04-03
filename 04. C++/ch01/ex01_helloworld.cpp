#include <iostream>
using namespace std;

int main(int argc, char const *argv[])
{
    cout << "Hello World" << endl;

    // using namespace std;를 사용 안하는 경우 namespace 필요
    std::cout << "Hello World" << std::endl;
    return 0;
}