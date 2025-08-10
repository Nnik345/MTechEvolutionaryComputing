#include <iostream>
#include <vector>
#include <stack>
using namespace std;

class DFSSearch {
private:
    vector<vector<int>> adj;
    int nodes;
    
public:
    DFSSearch() : nodes(7) {
        adj.resize(7);
        adj[0] = {1, 2};
        adj[1] = {3, 4};
        adj[2] = {3, 5};
        adj[3] = {6};
        adj[4] = {6};
        adj[5] = {6};
    }
    
    bool dfsRecursive(int current, int goal, vector<bool>& visited, vector<int>& path) {
        visited[current] = true;
        path.push_back(current);
        
        if (current == goal) {
            return true;
        }
        
        for (int neighbor : adj[current]) {
            if (!visited[neighbor]) {
                if (dfsRecursive(neighbor, goal, visited, path)) {
                    return true;
                }
            }
        }
        
        path.pop_back();
        return false;
    }
    
    void search(int start, int goal) {
        vector<bool> visited(nodes, false);
        vector<int> path;
        
        cout << "DFS Result:" << endl;
        if (dfsRecursive(start, goal, visited, path)) {
            cout << "Path found: ";
            for (int node : path) {
                cout << node << " ";
            }
            cout << endl;
        } else {
            cout << "No path found!" << endl;
        }
    }
};

int main() {
    DFSSearch dfs;
    dfs.search(0, 6);
    return 0;
}
