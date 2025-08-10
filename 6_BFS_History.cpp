#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class BFSHistorySearch {
private:
    vector<vector<int>> adj;
    int nodes;
    vector<int> explorationOrder;
    vector<int> levelOrder;

public:
    BFSHistorySearch() : nodes(7) {
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
        vector<int> parent(nodes, -1);
        vector<int> level(nodes, 0);
        queue<int> q;

        explorationOrder.clear();
        levelOrder.clear();

        visited[start] = true;
        level[start] = 0;
        q.push(start);

        while (!q.empty()) {
            int current = q.front();
            q.pop();

            explorationOrder.push_back(current);
            levelOrder.push_back(level[current]);

            if (current == goal) {
                vector<int> path;
                int node = goal;
                while (node != -1) {
                    path.push_back(node);
                    node = parent[node];
                }
                reverse(path.begin(), path.end());

                cout << "BFS+History Result:" << endl;
                cout << "Path found: ";
                for (int n : path) {
                    cout << n << " ";
                }
                cout << endl;
                
                return;
            }

            for (int neighbor : adj[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parent[neighbor] = current;
                    level[neighbor] = level[current] + 1;
                    q.push(neighbor);
                }
            }
        }

        cout << "No path found!" << endl;
    }
};

int main() {
    BFSHistorySearch bfsHistory;
    bfsHistory.search(0, 6);
    return 0;
}
