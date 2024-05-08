#include <iostream>
using namespace std;

int main() {
    int n;

    cout << "Enter the size of the array: ";
    cin >> n;
    int arr[n];
    cout << "Enter " << n << " elements for the array:\n";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];}
    cout << "The elements of the array in reversed order are: ";
    for (int i = n - 1; i >= 0; i--) {
        cout << arr[i] << " ";  // Print from the end to the beginning
    }



}
