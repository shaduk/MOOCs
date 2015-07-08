import java.util.Scanner;
public class vigenere
{
    
public static void main(String[] arg)
{
    System.out.println("Enter the massage");
    Scanner scan =new Scanner(System.in);
    String s =scan.nextLine();
    
    System.out.println("Enter the key");
    Scanner key =new Scanner(System.in);
    String k =key.nextLine();
    
    
    for(int i=0,j=0;i<s.Length;j<k.length;i++)
    {
            
        char c = s.charAt(i);
        
        int ASCII = (int ) c;
        
    if(ASCII>96 && ASCII<123)
     
    {
        char c2 = k.charAt(j);
        int ASCII2 = (int) c2; 
        ASCII= ((ASCII-97+ASCII2-97)%26)+97;
        j = j+1;
    }
    
    else if(ASCII>64 && ASCII<91)
    {
        char c3 = k.charAt(j);
        int ASCII3 = (int) c3; 
        ASCII= ((ASCII-65+ASCII3-97)%26)+65;
        j=j+1;
    }
     
        
    
     else 
     {
         
        
     }
        char b = (char) ASCII;
        System.out.print(b);
            
            
            
    }
        
    
}

}