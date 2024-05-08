#include <iostream>

using namespace std;

class Node {
public:
    int data;
    Node* prev;
    Node* next;
};

class CircularQueue {
public:
    Node* head;
    Node* tail;

    CircularQueue() {
        head = nullptr;
        tail = nullptr;
    }

    void enqueue(int value) {
        Node* newNode = new Node();
        newNode->data = value;

        if (tail == nullptr) {
            head = tail = newNode;
            head->next = head;
            head->prev = head;
        } else {
            tail->next = newNode;
            newNode->prev = tail;
            newNode->next = head;
            head->prev = newNode;
            tail = newNode;
        }
    }

    int dequeue() {
        if (head == nullptr) {
            cerr << "Queue is empty!" << endl;
            return -1;
        }

        int value = head->data;
        if (head == tail) {
            delete head;
            head = tail = nullptr;
        } else {
            Node* oldHead = head;
            head = head->next;
            tail->next = head;
            head->prev = tail;
            delete oldHead;
        }

        return value;
    }

    void traverse() {
        if (head == nullptr) {
            cout << "Queue is empty!" << endl;
            return;
        }

        Node* current = head;
        do {
            cout << current->data << " -> ";
            current = current->next;
        } while (current != head);
        cout << "HEAD (circular)" << endl;
    }


    ~CircularQueue() {
        if (head == nullptr) {
            return;
        }

        Node* current = head;
        do {
            Node* toDelete = current;
            current = current->next;
            delete toDelete;
        } while (current != head);

        head = tail = nullptr;
    }
};

int main() {
    CircularQueue queue;


    queue.enqueue(3);
    queue.enqueue(4);
    queue.enqueue(5);
    queue.enqueue(6);

    cout << "Initial Circular Queue: ";
    queue.traverse();  // Expected is 3 -> 4 -> 5 -> 6 -> HEAD


    int dequeuedValue = queue.dequeue();  // this dequeue the front element
    cout << "Dequeued: " << dequeuedValue << endl;

    cout << "Queue after dequeue: ";
    queue.traverse();  // prints 4 -> 5 -> 6 -> HEAD (circular)

    return 0;
}
