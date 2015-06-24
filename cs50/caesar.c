#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main(int argc, char* argv[])
{
    if(argc!=2)
    {
        return 1;
    }
    int k = atoi(argv[1]);
    char text[100];
    fgets(text, 100, stdin); 
   
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        if(text[i]>='A' && text[i]<='Z')
        {
            printf("%c", (text[i]-65+k)%26 + 65);  
        }
        else if(text[i]>='a' && text[i]<='z')
        {
            printf("%c", (text[i]-97+k)%26 + 97);  
        }
    }
    return 0;
    
}