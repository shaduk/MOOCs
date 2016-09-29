
//*************** Client Program *************

class BST {
	public static void main(String args[]) {
		 Tree tr;
		 tr = new Tree(100);
		 tr.insert(50);
		 tr.insert(125);
		 tr.insert(150);
		 tr.insert(25);
		 tr.insert(75);
		 tr.insert(20);	
		 tr.insert(90);
		tr.delete(20);
		 tr.delete(20);
		 tr.delete(125);
		 tr.delete(150);
		 tr.delete(100);
		 tr.delete(50);
		 tr.delete(75);
		 tr.delete(25);
		 tr.delete(90); 
		 
	}
}

class Tree { // Defines one node of a binary search tree
	
	public Tree(int n) {
		value = n;
		left = null;
		right = null;
	}
	
	public void insert(int n) {
		if (value == n)
			return;
		if (value < n)
			if (right == null)
				right = new Tree(n);
			else
				right.insert(n);
		else if (left == null)
			left = new Tree(n);
		else
			left.insert(n);
	}

	public Tree min() {
		if(left == null)
			return this;
		else
			return left.min();
	}
	
	public Tree max(){
		if(right == null)
			return this;
		else
			return right.max();
	}
	
	public Tree find(int n)
	{
		if(n == value)
			return this;
		else if(n > value && right!=null)
			return right.find(n);
		else if(n < value && left!=null)
			return left.find(n);
		else
			return null;
	}
	
	public Tree findParent(int n, Tree parent)
	{
		if(n == value)
			return parent;
		else if(n > value && right!=null)
			return right.findParent(n, this);
		else if(n < value && left!=null)
			return left.findParent(n, this);
		else
			return null;
	}
	
	public void case1(int n, Tree tr, Tree parent)
	{
		if(tr == parent)
		{
			System.out.print("Parent node with both subtrees null cannot be deleted");
			return;
		}
		if(parent.left!= null && parent.left.value == n)
			parent.left = null;
		else
			parent.right = null;
	}
	
	public void case2(int n, Tree tr, Tree parent)
	{
		if(parent == tr)
		{
			if(parent.left!=null)
			{
				parent.value = parent.left.max().value;
				parent.left.delete(parent.value);
			}
			else
			{
				parent.value = parent.right.max().value;
				parent.right.delete(parent.value);
			}
		}
		else if(parent.left!=null && parent.left.value == n)
			parent.left = parent.left.left;
		else
			parent.right = parent.right.right;
		
	}
	
	public void case3(int n, Tree tr, Tree parent)
	{
		int min = tr.right.min().value;
		
		tr.value = min;
		
		if(min == tr.right.value)
			tr.right = tr.right.right;
		else
		tr.right.delete(min);
	}
	
	
	public void delete(int n) {  

	// fill in the code for delete
		
		Tree tr = find(n);
		Tree parent = findParent(n, this);
		
		if(tr == null)
		{
			System.out.println("The tree is not present in Binary Tree");
			return;
		}
		if(tr.left == null && tr.right == null)
		{

			case1(n, tr, parent);

		}
		else if((tr.left == null) || (tr.right == null))
		{
			
			case2(n, tr, parent);
		}
		else
		{
			case3(n, tr, parent);
		} 
		
	}
	
	protected int value;
	protected Tree left;
	protected Tree right;
}

























