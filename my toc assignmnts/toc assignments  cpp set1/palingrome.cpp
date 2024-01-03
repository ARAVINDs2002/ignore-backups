#include<iostream>
using namespace std;

int main() {
int i,rev=0,num,rem;
cout<<"enter limit";
cin>>num;
int orgnl=num;
while(num!=0)
{
    rem=num%10;
    rev=rev*10+rem;
    num=num/10;
    if(rev==orgnl)
    {   cout<<"hey its poalngrome ....";

            break;
    }

}
 cout<<rev;

    return 0;
}
