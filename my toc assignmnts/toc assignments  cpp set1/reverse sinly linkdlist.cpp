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
node*reverse(node*head)
{
    node*current=head;
    node*prev=nullptr;
    node*next=nullptr;
   while(current!=nullptr)
    {
        next=current->next;
   current->next=prev;
   prev=current;
   current=next;
    }
    return prev;
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
    cout<<"priting original array  :\n";
    print(head);
    cout<<endl;
     cout<<"priting reverese array  :\n";
    head=reverse(head);
    print(head);

}
