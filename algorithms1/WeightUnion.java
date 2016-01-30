public class WeightUnion
{
    private int[] id;
    private int[] sz;
    public WeightUnion(int N)
    {
        id = new int[N];
        sz = new int[N];
        for (int i = 0; i < N; i++) sz[i] = 1;
        for(int i=0; i < N; i++)
            id[i] = i;
    }
    
    private int root(int i)
    {
        while(i != id[i])
        {
            i = id[i];
        }
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
        if (sz[i] < sz[j])
        {
            id[i] = j;
            sz[j] += sz[i];
        }
        else
        {
            id[j] = i;
            sz[i] += sz[j];
        }
        
    }
    
     
    public static void main(String[] args) {
        WeightUnion q = new WeightUnion(10);
        q.union(4, 3);
        q.union(3, 8);
        q.union(6, 5);
        q.union(9, 4);
        q.union(2, 1);
        q.union(5, 0);
        q.union(7, 2);
        q.union(6, 1);
        q.union(7, 3);
        for (int i = 0; i < 10; i++) 
            System.out.print(q.id[i] + " ");
            System.out.print("\n");
    }
    
}