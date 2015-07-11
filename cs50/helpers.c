/**
 * helpers.c
 *
 * Computer Science 50
 * Problem Set 3
 *
 * Helper functions for Problem Set 3.
 */

#include <cs50.h>

#include "helpers.h"

/**
 * Returns true if value is in array of n values, else false.
 */
bool search(int value, int values[], int n)
{
   int first = 0;
   int last = n-1; 
   while(true)
   {
      
     int middle = (first + last)/2;
     if(first > last)
     {
        return false;
     }
        
     if(values[middle] == value)
     {
        return true;
     }
     else if(value > values[middle])
     {
        first = middle+1;
     }
     else if(value < values[middle])
     {
        last = middle-1;
     }
      
   }
    
}

/**
 * Sorts array of n values.
 */
void sort(int values[], int n)
{
    // TODO: implement an O(n^2) sorting algorithm
    if(n!=0)
    {
        for(int i=0; i < n; i++)
        {
            for(int j=i+1; j < n; j++)
            {
                if(values[i] > values[j])
                {
                    int temp=0;
                    temp = values[i];
                    values[i] = values[j];
                    values[j] = temp;
                }
            }
        }
    }
    return;
}
 