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

    void reverse() {
        Node* prev = nullptr;
        Node* current = head;
        Node* next = nullptr;

        while (current != nullptr) {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        head = prev;
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

    list.reverse();

    cout << "Reversed list: ";
    list.traverse();

    return 0;
}
