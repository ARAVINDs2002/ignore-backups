#include <iostream>
using namespace std;

class TwoStacks {
private:
    int* arr;
    int size;
    int top1;
    int top2;

public:

    TwoStacks(int n) {
        size = n;
        arr = new int[n];
        top1 = -1;
        top2 = n;
    }


    void push1(int value) {
        if (top1 < top2 - 1) {
            top1++;
            arr[top1] = value;
        } else {
            cout << "Stack 1 Overflow!" << endl;
        }
    }


    void push2(int value) {
        if (top1 < top2 - 1) {
            top2--;
            arr[top2] = value;
        } else {
            cerr << "Stack 2 Overflow!" << endl;
        }
    }


    int pop1() {
        if (top1 >= 0) {
            int value = arr[top1];
            top1--;
            return value;
        } else {
            cout << "Stack 1 Underflow!" << endl;
            return -1;
        }
    }

    int pop2() {
        if (top2 < size) {
            int value = arr[top2];
            top2++;
            return value;
        } else {
            cerr << "Stack 2 Underflow!" << endl;
            return -1;
        }
    }

    ~TwoStacks() {
        delete[] arr;
    }
};

int main() {
    TwoStacks stacks(10);
    stacks.push1(1);
    stacks.push1(2);
    stacks.push2(10);
    stacks.push2(9);
    cout << "Pop from Stack 1: " << stacks.pop1() << endl;  // Should be 2
    cout << "Pop from Stack 2: " << stacks.pop2() << endl;  // Should be 9

    return 0;
}
