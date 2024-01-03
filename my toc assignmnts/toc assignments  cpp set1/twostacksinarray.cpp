#include<iostream>
using namespace std;
class my2stack
{ private:
    int*array;
    int size;
    int top1;
    int top2;

public:
    my2stack(int size)
    {
        this->array=new int[size];
        this->size=size;
        this->top1=-1;
        this->top2=size;
    }
    void push1(int element)
    {
        if(top1<top2-1)
        {
            top1++;
            array[top1]=element;
            cout<<"pushed  "<<"element"<<element<<endl;
        }
    }
    void push2(int element)
    {
        if(top1<top2-1)
        {
            top2--;
            array[top2]=element;
            cout<<"pushed  "<<"element"<<element<<endl;
        }
    }
};

int main()
{
    my2stack stack(10);
    stack.push1(1);
     stack.push1(2);
      stack.push1(3);
       stack.push1(4);
        stack.push1(5);
        cout<<endl;
        cout<<"****************end of stack 1****************\n";
         stack.push2(6);
          stack.push2(7);
           stack.push2(8);
           stack.push2(9);
              cout<<endl;
        cout<<"****************end of stack 2****************";

}
