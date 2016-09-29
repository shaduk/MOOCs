#include <iostream>
#include <vector>

using namespace std;

bool visited[100];
vector<int> graph[1000];

void initialize()
{
    for(long long int i = 0;i < 100;++i)
     	visited[i] = false;
    for(long long int i = 0; i < 1000; i++)
    	graph[i].clear();
}

void dfs(int s, int p)
{
    visited[s] = true;
    cout << s << " ";
    
    for(int i = 0; i < graph[s].size(); i++)
    {   
        if(visited[graph[s][i]] && graph[s][i] != p)
            {
            cout << "There is a Cycle" << endl;
            return;
            }
        if(!visited[graph[s][i]])
        dfs(graph[s][i], s);
    }
}


int main()
{

    int V, E;
    cin >> V >> E;
     initialize();
    while(E--)
    {
        int a, b;
        cin >> a >> b;
        graph[a].push_back(b);
        
    }
    
    for(int i = 1; i <= V; i++)
    {
        if(!visited[i])
        dfs(i, 0);
    }
}