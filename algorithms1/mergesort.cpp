#include <iostream>
using namespace std;

void Merge(int Arr[], int start, int end, int mid)
{
    for(int i = start; i <= end; i++)
    {
        cout << Arr[i];
    }
    cout << endl;
    
    int i = start, j = mid + 1; 
    int k = 0;
    int Aux[end - start + 1];
    
    while(i <= mid && j <= end)
    {
        if(Arr[i] >= Arr[j])
        {
            Aux[k] = Arr[j];
            k++;
            i++;
            j++;
        }
        else if(Arr[j] >= Arr[i])
        {
            Aux[k] = Arr[i];
            k++;
            j++;
            i++;
        }
            
    }
    while(i <= mid)
    {
        Aux[k] = Arr[i];
        k++;
        i++;
    }
    while(j <= end)
    {
        Aux[k] = Arr[j];
        k++;
        j++;
    }
    for(int l = 0; l < end - start + 1; l++)
    {
        Arr[start] = Aux[0];
        start++;
    }
    
    
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
    
    int Arry[8] = {4,3,1,2,7,8,5,3};
    MergeSort(Arry, 0, 7);

    for(int i = 0; i < 8; i++)
    {
        cout << Arry[i];
    }
}
