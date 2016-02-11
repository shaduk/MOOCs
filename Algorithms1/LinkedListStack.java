

public class LinkedListStack
{
    private Node first = null;
    
    private class Node 
    {
        String item;
        Node next;
    }
    
    public boolean isEmpty()
    {
        return first == null;
    }
    
    public void push(String item)
    {
        Node oldfirst = first;
        first = new Node();
        first.item = item;
        first.next = oldfirst;
    }
    
    public String pop()
    {
        String item = first.item;
        first = first.next;
        return item;
    }
    
    public static void main(String[] args)
    {
        LinkedListStack stack = new LinkedListStack();
        stack.push("shad");
        stack.push("khan");
        System.out.print(stack.pop());
        System.out.print(stack.pop());
    }
}

