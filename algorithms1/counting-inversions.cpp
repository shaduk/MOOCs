

#include <iostream>
#include <fstream>
#include <string>
using namespace std;
int total = 0;

void Merge(int Arr[], int start, int end, int mid)
{
    int i = start, j = mid + 1;
    int k = 0;
    int lengthaux = end - start + 1;
    int Aux[lengthaux];
    
    while(i <= mid && j <= end)
    {
        if(Arr[i] >= Arr[j])
        {
            Aux[k++] = Arr[j++];
            total = total + mid - i + 1;
        }
        else if(Arr[j] >= Arr[i])
        {
            Aux[k++] = Arr[i++];
            
        }
    }
    
    while(i <= mid)
    {
        Aux[k++] = Arr[i++];
        
    }
    
    while(j <= end)
    {
        Aux[k++] = Arr[j++];
        
    }
    
    for(int l = 0; l < lengthaux; l++)
    {
        Arr[start] = Aux[l];
        start++;
    }
    cout << "total " << total << endl;
}

void MergeSort(int Arr[], int start, int end)
{
    if(start < end){
        int mid = (start + end) / 2;
        MergeSort(Arr, start, mid);
        MergeSort(Arr, mid+1, end);
        Merge(Arr, start, end, mid);
    }
}

int main()
{
    
    ifstream infile("IntegerArray.txt");
   
    int Arry[100000];
    int i = 0, a;
    while (infile >> a)
    {
        Arry[i++] = a;
    }
    
    MergeSort(Arry, 0, 100000-1);
    for(int i = 0; i < 100000; i++)
    {
        cout << Arry[i] << " ";
    }
    cout << endl;
    
}