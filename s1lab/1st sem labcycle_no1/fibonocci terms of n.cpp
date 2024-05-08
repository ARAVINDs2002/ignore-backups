#include <iostream>
using namespace std;

int main() {
    int a = 0, b = 1, c, i, n;
    int z=1;
    cout << "Enter the number of terms: ";
    cin >> n;
    cout << a << " ";
    cout << b << " ";
    for (i = 2; i < n; i++) {
        c = a + b;
        z=z+c;
        a = b;
        b = c;
        cout << c <<" ";
    }
    cout<<endl;
     cout <<"the sum is "<< z << endl;
}
