#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next = nullptr;
};

class SinglyLinkedList {
public:
    Node* head = nullptr;

    void insert_in_between(int position, int value) {
        if (position < 0) {
            cout << "Invalid position." << endl;
            return;
        }

        if (position == 0) {
            Node* newNode = new Node;
            newNode->data = value;
            newNode->next = head;
            head = newNode;
            return;
        }

        Node* newNode = new Node;
        newNode->data = value;

        Node* current = head;
        int i = 0;

        while (current != nullptr && i < position - 1) {
            current = current->next;
            i++;
        }

        if (current == nullptr) {
            cout << "Position out of bounds." << endl;
            delete newNode;
            return;
        }

        newNode->next = current->next;
        current->next = newNode;
    }

    void insert_at_beginning(int value) {
        Node* newNode = new Node;
        newNode->data = value;
        newNode->next = head;
        head = newNode;
    }

    void insert_at_end(int value) {
        Node* newNode = new Node;
        newNode->data = value;
        newNode->next = nullptr;

        if (head == nullptr) {
            head = newNode;
        } else {
            Node* current = head;
            while (current->next != nullptr) {
                current = current->next;
            }
            current->next = newNode;
        }
    }

    void traverse() {
        Node* current = head;
        while (current != nullptr) {
            cout << current->data << " -> ";
            current = current->next;
        }
        cout << "null" << endl;
    }
};

int main() {
    SinglyLinkedList list;

    list.insert_at_beginning(1);
    list.insert_at_end(3);
    list.insert_at_end(4);

    list.insert_in_between(1, 99);
    list.insert_in_between(2, 98);
    list.traverse();


    return 0;
}
