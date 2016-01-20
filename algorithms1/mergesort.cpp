#include <iostream>


void Merge(int Arr[], int start, int end, int mid)
{
    int i = start, j = mid + 1; 
    int k = 0;
    int Aux[end - start + 1];
    
    while(i <= mid && j <= end)
    {
        if(Arr[i] >= Arr[j])
        {
            Aux[k] = Arr[j];
            k++;
        }
        else if(Arr[j] >= Arr[i])
        {
            Aux[k] = Arr[i];
            k++;
        }
            
    }
    while(i <= mid)
    {
        Aux[k] = Arr[i];
    }
    while(j <= end)
    {
        Aux[k] = Arr[j];
    }
    for(int l = 0; l < end - start + 1; l++)
    {
        Arr[start] = Aux[0];
        start++;
    }
    
}

int MergeSort(int Arr[], int start, int end)
{
   if(start < end){
    int mid = (start + end) / 2;
    MergeSort(Arr, start, mid);
    MergeSort(Arr, mid+1, end);
    Merge(Arr, start, end, mid);
   }
}

int Arry[8] = {4,3,1,2,7,8,5,3};
MergeSort(Arry[], 0, 7);

for(int i = 0; i < 8; i++)
{
    cout << Arry[i];
}

