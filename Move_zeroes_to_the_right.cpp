#include<iostream>
#include<vector>
#include<array>
#include<string>
#include<iterator>
#include<algorithm>
using namespace std;

int main()
{
	int n;
	cout<<"Enter the no of elements : "<<endl;
	cin>>n;
	
	int num =n;
	
	int arr[n];
	cout<<"Enter array elements : "<<endl;
	for(int i=0; i<n; i++)
	{
		cin>>arr[i];
	}
	cout<<"Array elements are : "<<endl;
	for(int i=0; i<n; i++)
	{
		cout<<arr[i]<<endl;
	}
	
	int i=0;
	while(i<n)
	{
		if(arr[i] == 0)
		{
			swap(arr[i],arr[n-1]);
			n--;
		}
		else
		{
			i++;
		}
	}
	for (int i=0; i<num; i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;
	
	return 0;
	
}
