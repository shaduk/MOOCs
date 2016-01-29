


public class QuickUnion
{
    private int[] id;
    
    public QuickUnion(int N)
    {
        id = new int[N];
        for(int i=0; i < N; i++)
            id[i] = i;
    }
    
    private int root(int i)
    {
        while(i != id[i]) i = id[i];
        return i;
    }
    
    public boolean connected(int p, int q)
    {
        return root(p) == root(q);
    }
    
    public void union(int p, int q)
    {
        int i = root(p);
        int j = root(q);
        id[i] = j;
        
    }
    
     
    public static void main(String[] args) {
        QuickUnion q = new QuickUnion(10);
        q.union(3, 8);
        q.union(5, 2);
        q.union(2, 3);
        q.union(9, 1);
        q.union(7, 4);
        q.union(3, 9);
        for (int i = 0; i < 10; i++) 
            System.out.print(q.id[i] + " ");
            System.out.print("\n");
    }
    
}