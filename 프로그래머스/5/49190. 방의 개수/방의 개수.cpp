#include <string>
#include <vector>
#include <iostream>
#include <algorithm>
#include <map>
#include <unordered_map>

using namespace std;

int dirr[] = { -1, -1, 0, 1, 1, 1, 0, -1 };
int dirc[] = { 0, 1, 1, 1, 0, -1, -1, -1 };

vector<pair<int, int>> vertex;
map<pair<int, int>, int> graph;
map<pair<int, int>, int> vis_node;
map<pair<int, int>, int> vis_edge;

int solution(vector<int> arrows) {
    int answer = 0;
    int sr = 0, sc = 0;

    vertex.push_back({sr, sc});
    for (int i = 0; i < arrows.size(); i++) {
        sr += dirr[arrows[i]];
        sc += dirc[arrows[i]];
        vertex.push_back({sr, sc});

        sr += dirr[arrows[i]];
        sc += dirc[arrows[i]];
        vertex.push_back({sr, sc});
    }

    int index = 0;
    for (auto& p : vertex) {
        if (graph.find(p) != graph.end()) {

        } else {
            graph[p] = index;
            index++;
        }
    }

    vis_node[vertex[0]] = 1;

    for (int i = 1; i < vertex.size(); i++) {
        pair<int, int> cp = vertex[i];
        pair<int, int> pp = vertex[i - 1];

        int cn = graph[cp];
        int pn = graph[pp];

        if (vis_node.find(cp) != vis_node.end() && vis_edge[{cn, pn}] == 0 && vis_edge[{pn, cn}] == 0) {
            answer++;
        }

        vis_edge[{cn, pn}]++;
        vis_edge[{pn, cn}]++;
        vis_node[cp] = 1;
    }

    return answer;
}