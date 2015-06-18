#include <stdio.h>
#include <cs50.h>
#include <math.h>

int main(void)
{
    float n,ncents;
    int ncentint,count=0;
    
    do
    {
        printf("O hai! How much change is owed? \n");
        n = GetFloat();
    }
    while(n<0);
    
    ncents = round(n*100);
    ncentint = (int)ncents;
    
    count = count + ncentint/25;
    ncentint = ncentint%25;
    count = count + ncentint/10;
    ncentint = ncentint%10;
    count = count + ncentint/5;
    ncentint = ncentint%5;
    count = count + ncentint;
    printf("%d\n",count);
}