import java.util.Scanner;

public class HelloWorld {

    public static void main(String[] args) {
        
        System.out.println("Enter the string");
        Scanner scan= new Scanner(System.in);
        String x = scan.nextLine();

        for(int i=0;i<x.length();i++)
        {
            char c= x.charAt(i);
     int ASCII =(int) c ;
     if(ASCII>96 && ASCII<123)
     
    { 
        ASCII= ((ASCII-97+3)%26)+97;
        
    }
    else if(ASCII>64 && ASCII<91)
    {
        ASCII= ((ASCII-65+3)%26)+65;
    }
     
        
    
     else 
     {
         
        System.out.println(x) ;
     }
        char b = (char) ASCII;
        System.out.print(b);
         
        }
    

            
    }  
}
