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

	sort(arr, arr+n);

	for (int i=0; i<n-1; i+=2)
	{
		swap(arr[i], arr[i+1]);
	}

	for (int i=0; i<n; i++)
	{
		cout<<arr[i]<<" ";
	}
	cout<<endl;

	return 0;
}
