#include<iostream>
using namespace std;
int main()
{
    int a,b,c,num;
    a=0;
    b=1;
    cout<<"enter limit";
    cin>>num;
    cout<<a;
    cout<<b;
    for(int i=2;i<=num;i++)
    {
        c=a+b;
        a=b;
        b=c;
        cout<<c;
    }
}
