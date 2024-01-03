#include<iostream>
using namespace std;
class node
{ public:
  int data;
  node*next ;
};
void insertatend(node*&head,int data)
{
    node*newnode=new node;
    newnode->data=data;
    newnode->next=nullptr;
    if(head==nullptr)
    {
        head=newnode;
    }
    else{

        node*current=head;
        while(current->next!=nullptr)
        {
            current=current->next;
        }
        current->next=newnode;
    }

}
void print(node*h)
{
    while(h!=nullptr)
    {
        cout<<h->data<<"--->";
        h=h->next;
    }
    cout<<"null";
}

int main()
{
    node*head=nullptr;
    insertatend(head,1);
    insertatend(head,2);
    insertatend(head,3);
    insertatend(head,4);
    insertatend(head,5);
    insertatend(head,6);

    print(head);
    cout<<endl;
    cout<<"*************completed insertion at end***************";


}
