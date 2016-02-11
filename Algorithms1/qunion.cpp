#include <iostream>

template<int N>
class quick_union{
public:
	quick_union()
	{
		for(int i =0; i < N; ++i){
			elements[i] = i;
		}
	}

	bool connected(int p, int q) const{
		// are they in the same connected component tree?
		int proot = root(p);
		int qroot = root(q);
		return (proot == qroot);
	}

	void union_components(int p, int q)
	{
		int proot = root(p);
		int qroot = root(q);
		elements[qroot] = proot;	
	}

private:

	int root(int p) const{
		while(elements[p] != p){
			p = elements[p]; 
		}
		return p;
	}

	int elements[N];
};

int main(){

	quick_union<10> q;

	q.union_components(0,1);
	q.union_components(1,2);

	using namespace std;

	cout << "Connected: " << boolalpha << (q.connected(0,1)) << endl;
	cout << "Connected: " << boolalpha << (q.connected(1,2)) << endl;
	cout << "Connected: " << boolalpha << (q.connected(2,2)) << endl;
	cout << "Connected: " << boolalpha << (q.connected(0,8)) << endl;

	return 0;
}