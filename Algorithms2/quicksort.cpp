#include <iostream>

using namespace std;

int partition(int Arry[], int start, int end)
{
    int pivot = Arry[end];
    int pindex = start;
    for(int i = start; i < end; i++)
    {
        if(Arry[i] <= pivot)
        {   
            int temp1 = Arry[pindex];
            Arry[pindex] =  Arry[i];
            Arry[i] = temp1;
            pindex++;
        }
    }
    int temp2 = Arry[pindex];
    Arry[pindex] =  Arry[end];
    Arry[end] = temp2;
    return pindex;
}


void QuickSort(int Arry[], int start, int end)
{
    if(start < end)
    {
        int pindex = partition(Arry, start, end);
        QuickSort(Arry, start, pindex-1);
        QuickSort(Arry, pindex+1, end);
    }
}

int main()
{
    int Arry[8] = {4,3,1,2,7,8,5,3};
    QuickSort(Arry, 0, 7);

    for(int i = 0; i < 8; i++)
    {
        cout << Arry[i];
    }
    cout << endl;
}