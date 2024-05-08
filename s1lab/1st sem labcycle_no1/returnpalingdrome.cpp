#include <iostream>
using namespace std;

// Function to reverse the digits of an integer
int getPalindrome(int num) {
    int reversed = 0;
    while (num > 0) {
        int digit = num % 10;
        reversed = reversed * 10 + digit;
        num =num/10;
    }
    return reversed;
}
int main() {
    int number;
    cout << "Enter a number: ";
    cin >> number;

    int palindrome = getPalindrome(number);
    cout << "Palindrome (reversed number): " << palindrome << endl;

    return 0;
}
