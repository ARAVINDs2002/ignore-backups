#include<iostream>
using namespace std;

int main() {
    int rows,cols;
cout<<"enter rows";
cin>>rows;
cout<<"enter cols";
cin>>cols;
int arr[rows][cols];
for(int i=0;i<rows;i++)
{
    for(int j=0;j<cols;j++)
    {
        cin>>arr[i][j];
    }
}
int max=arr[0][0];
for(int i=0;i<rows;i++)
{

    for(int j=0;j<cols;j++)
    {
        if(arr[i][j]>max)
        {
            max=arr[i][j];
        }
    }

}
cout<<"max is"<<max;
}
