#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

class BFSSearch {
private:
    vector<vector<int>> adj;
    int nodes;

public:
    BFSSearch() : nodes(7) {
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
        queue<int> q;

        visited[start] = true;
        q.push(start);

        bool found = false;
        while (!q.empty()) {
            int current = q.front();
            q.pop();

            if (current == goal) {
                found = true;
                break;
            }

            for (int neighbor : adj[current]) {
                if (!visited[neighbor]) {
                    visited[neighbor] = true;
                    parent[neighbor] = current;
                    q.push(neighbor);
                }
            }
        }

        cout << "BFS Result:" << endl;
        if (found) {
            vector<int> path;
            for (int v = goal; v != -1; v = parent[v]) {
                path.push_back(v);
            }
            reverse(path.begin(), path.end());

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
    BFSSearch bfs;
    bfs.search(0, 6);
    return 0;
}
