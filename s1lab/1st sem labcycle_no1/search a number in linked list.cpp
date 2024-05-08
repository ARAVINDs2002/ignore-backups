#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* next;
};

class SinglyLinkedList {
public:
    Node* head = nullptr;

    void insert(int value) {
        Node* newNode = new Node();
        newNode->data = value;
        newNode->next = head;
        head = newNode;
    }

    void traverse() {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "null" << endl;
    }
     void finder(int target) {
        Node* current = head;
        int index = 0;
        bool found = false;

        while (current != nullptr) {
            if (current->data == target) {
                found = true;
                break;
            }
            current = current->next;
            index++;
        }

        if (found) {
            cout << "Value " << target << " found at index " << index << "." << endl;
        } else {
            cout << "Value " << target << " not found in the list." << endl;
        }
    }

};

int main() {
    SinglyLinkedList list;

    list.insert(6);
    list.insert(5);
    list.insert(4);
    list.insert(3);

    cout << "Original list: ";
    list.traverse();
    list.finder(4);





    return 0;
}

