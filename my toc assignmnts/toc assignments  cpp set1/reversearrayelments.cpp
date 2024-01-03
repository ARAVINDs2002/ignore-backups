#include<iostream>
using namespace std;
int main()
{
    int size;
    cout<<"enter total size";
    cin>>size;
    int arr[size];
cout<<"enter array elements\n";
    for(int i=0;i<size;i++)
    {
        cin>>arr[i];
    }
    cout<<"reverse array elements are\n";
     for(int i=size-1;i>=0;i--)
    {
        cout<<arr[i]<<" ";
    }
}
