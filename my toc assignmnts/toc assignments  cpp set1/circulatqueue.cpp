#include <iostream>
using namespace std;

class Node {
public:
    int data;
    Node* next;
    Node* prev;
};

class CircularQueue {
private:
    Node* front;
    Node* rear;

public:
    CircularQueue() {
        front = nullptr;
        rear = nullptr;
    }

    bool isEmpty() {
        return (front == nullptr);
    }

    void enqueue(int data) {
        Node* newNode = new Node;
        newNode->data = data;

        if (isEmpty()) {
            front = newNode;
            rear = newNode;
            front->next = rear;
            rear->prev = front;
        } else {
            rear->next = newNode;
            newNode->prev = rear;
            rear = newNode;
            rear->next = front;
            front->prev = rear;
        }
    }



    int getFront() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return -1;
        }
        return front->data;
    }

    void display() {
        if (isEmpty()) {
            cout << "Queue is empty." << endl;
            return;
        }

        Node* current = front;
        do {
            cout << current->data << " ";
            current = current->next;
        } while (current != front);

        cout << endl;
    }


};

int main() {
    CircularQueue queue;

    queue.enqueue(1);
    queue.enqueue(2);
    queue.enqueue(3);
    queue.enqueue(4);

    cout << "Queue elements: ";
    queue.display();

    cout << "Front element: " << queue.getFront() << endl;



    return 0;
}
