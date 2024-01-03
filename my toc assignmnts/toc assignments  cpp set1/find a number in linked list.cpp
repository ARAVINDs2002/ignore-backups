#include<iostream>
using namespace std;
class node
{ public:
  int data;
  node*next ;
};
void insert(node*&head,int data)
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
        cout<<h->data<<"->";
        h=h->next;
    }
    cout<<"null";
}
void find(node*h,int target)
{int pos=0;
    while(h!=nullptr)
    {
        if(h->data==target)
        {
            cout<< "found at"<<pos;
            }

           h=h->next;
            pos++;
    }
}
int main()
{
    node*head=nullptr;
    insert(head,1);
    insert(head,2);
    insert(head,3);
    insert(head,4);
    insert(head,5);
    insert(head,6);
    print(head);
    cout<<endl;
    find(head,3);

}
