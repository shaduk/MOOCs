#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <ctype.h>

int main(int argc, char* argv[])
{
    if(argc!=2)
    {
        return 1;
    }
    
    int lenarg = strlen(argv[1]);
    
    char text[100];
    fgets(text, 100, stdin); 
    int j = -1;
    for(int i = 0, n = strlen(text); i < n; i++)
    {
        
        if(text[i]>='A' && text[i]<='Z')
        {
            j = j+1;
            int k = (int)tolower(argv[1][j%lenarg]);
            
            printf("%c", (text[i]-65+k-97)%26 + 65);  
        }
        else if(text[i]>='a' && text[i]<='z')
        {
            j = j + 1;
            int k = (int)tolower(argv[1][j%lenarg]);
            
            printf("%c", (text[i]-97+k-97)%26 + 97);  
        }
        
        else
        {
            j = j;
            printf(" ");
        }
    }
    printf("\n");
    return 0;
    
}