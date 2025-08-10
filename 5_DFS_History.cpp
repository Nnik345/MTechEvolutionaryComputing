#include <iostream>
#include <vector>
#include <set>
using namespace std;

class DFSHistorySearch {
private:
    vector<vector<int>> adj;
    int nodes;
    vector<int> foundPath;
    set<int> visitedNodes;
    
    bool dfsWithHistory(int current, int goal, vector<int>& path, vector<bool>& visited) {
        visited[current] = true;
        path.push_back(current);
        visitedNodes.insert(current);

        if (current == goal) {
            foundPath = path;
            return true;
        }

        for (int neighbor : adj[current]) {
            if (!visited[neighbor]) {
                if (dfsWithHistory(neighbor, goal, path, visited)) {
                    return true;
                }
            }
        }

        path.pop_back();
        visited[current] = false;
        return false;
    }
    
public:
    DFSHistorySearch() : nodes(7) {
        adj.resize(7);
        adj[0] = {1, 2};
        adj[1] = {3, 4};
        adj[2] = {3, 5};
        adj[3] = {6};
        adj[4] = {6};
        adj[5] = {6};
    }
    
    void search(int start, int goal) {
        vector<bool> visited(nodes, false);
        vector<int> path;
        foundPath.clear();
        visitedNodes.clear();
        
        bool pathFound = dfsWithHistory(start, goal, path, visited);
        
        cout << "DFS+History Result:" << endl;
        if (pathFound) {
            cout << "Path found: ";
            for (int node : foundPath) {
                cout << node << " ";
            }
            cout << endl;
        } else {
            cout << "No path found!" << endl;
        }
        cout << endl;
    }
};

int main() {
    DFSHistorySearch dfsHistory;
    dfsHistory.search(0, 6);
    return 0;
}