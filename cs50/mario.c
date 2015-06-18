#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    printf("Height: ");
    n = GetInt();
    
    while(n<0 || n>23)
    {
        printf("Height: ");
        n = GetInt();
    }
    
    for(int i=n;i>0;i--)
    {
        for(int j=i-1;j>0;j--)
            {
                printf(" ");
            }
        for(int k=n+2-i;k>0;k--)
            {   
                printf("#");
            }
        printf("\n");
    } 
    
}