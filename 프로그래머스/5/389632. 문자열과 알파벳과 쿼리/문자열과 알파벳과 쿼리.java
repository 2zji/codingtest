import java.util.*;

public class Solution {
    
    int groupId = 0;
    
    class SegmentTree {
        
        int N, M;
        int[] tree;
        int[] lazy;
        List<Integer> groups = new ArrayList<>();
        Map<Integer, Integer> map = new HashMap<>();
        int[] parent;
    
        public SegmentTree(int N, int M) {
            this.N = N;
            this.M = M;
            this.tree = new int[4*N];
            this.lazy = new int[4*N];
            this.parent = new int[M+1];
            for (int i=0; i<=M; i++) parent[i] = i;
    
            groups.add(0);
            map.put(0, 0);
        }
    
        int find(int x) {
            if (parent[x] == x) return x;
            return parent[x] = find(parent[x]);
        }
    
        void union(int x, int y) {
            if (!map.containsKey(y)) return;
            if (!map.containsKey(x)) {
                groups.add(x);
                map.put(x, groups.size()-1);
            }
            int px = find(map.get(x));
            int py = find(map.get(y));
            if (px != py) parent[py] = px;
        }
    
        void updateLazy(int node, int start, int end) {
            if (lazy[node] != 0) {
                tree[node] = lazy[node];
                if (start != end) {
                    lazy[node*2] = lazy[node];
                    lazy[node*2+1] = lazy[node];
                }
                lazy[node] = 0;
            }
        }
    
        void update(int node, int start, int end, int left, int right, int val) {
            updateLazy(node, start, end);
            if (left > end || right < start) return;
            if (left <= start && end <= right) {
                tree[node] = val;
                if (start != end) {
                    lazy[node*2] = val;
                    lazy[node*2+1] = val;
                }
                return;
            }
            update(node*2, start, (start+end)/2, left, right, val);
            update(node*2+1, (start+end)/2+1, end, left, right, val);
            tree[node] = Math.max(tree[node*2], tree[node*2+1]);
        }
    
        int query(int node, int start, int end, int idx) {
            updateLazy(node, start, end);
            if (idx < start || idx > end) return 0;
            if (start == end) return tree[node];
            int lval = query(node*2, start, (start+end)/2, idx);
            int rval = query(node*2+1, (start+end)/2+1, end, idx);
            return Math.max(lval, rval);
        }
    
        int query(int x) {
            return find(query(1, 1, N, x));
        }
        
        int getGroupId(int x) {
            return groups.get(query(x));
        }
        
        void move(int x, int newGroup) {
            if (!map.containsKey(x)) return;
            int idx = find(map.get(x));
            int oldGroup = groups.get(idx); 
            groups.set(idx, newGroup);
            map.remove(oldGroup);
            map.put(newGroup, idx);
        }
        
        void move(int left, int right, int newGroup) {
            groups.add(newGroup);
            int newIdx = groups.size() - 1;
            map.put(newGroup, newIdx);
            update(1, 1, N, left, right, newIdx);
        }
        
    }

    public int[] convert(String s) {
        int[] res = new int[s.length()];
        for (int i = 0; i < s.length(); i++) {
            res[i] = s.charAt(i) - 'a';
        }
        return res;
    }

    public String[] solution(String s, String[] query) {
        int[] codes = convert(s);
        int N = codes.length;
        int M = query.length;
        
        SegmentTree[] stArr = new SegmentTree[26];
        for (int i = 0; i < 26; i++) {
            stArr[i] = new SegmentTree(N, M);
        }

        List<String> answer = new ArrayList<>();

        for (String q : query) {
            String[] tokens = q.split(" ");
            String type = tokens[0];

            if (type.equals("1")) {
                int x = Integer.parseInt(tokens[1]);
                int y = Integer.parseInt(tokens[2]);
                int groupX = stArr[codes[x-1]].getGroupId(x);
                int groupY = stArr[codes[y-1]].getGroupId(y);
                answer.add(groupX == groupY ? "YES" : "NO");
            } else if (type.equals("2")) {
                int x = Integer.parseInt(tokens[1]);
                int[] word = convert(tokens[2]);
                Set<Integer> set = new HashSet<>();
                for (int ch : word) set.add(ch);

                int groupX = stArr[codes[x-1]].getGroupId(x);
                groupId++;
                for (int ch : set) {
                    stArr[ch].move(groupX, groupId);
                }
            } else if (type.equals("3")) {
                int x = Integer.parseInt(tokens[1]);
                int y = Integer.parseInt(tokens[2]);
                int[] word = convert(tokens[3]);
                Set<Integer> set = new HashSet<>();
                for (int ch : word) set.add(ch);
                
                groupId++;
                for (int ch : set) {
                    stArr[ch].move(x, y, groupId);
                }
            } else if (type.equals("4")) {
                int x = Integer.parseInt(tokens[1]);
                int y = Integer.parseInt(tokens[2]);
            
                int groupX = stArr[codes[x-1]].getGroupId(x);
                int groupY = stArr[codes[y-1]].getGroupId(y);
                
                if (groupX > groupY) {
                    int temp = groupX;
                    groupX = groupY;
                    groupY = temp;
                }
            
                for (SegmentTree st : stArr) {
                    st.union(groupX, groupY);
                }
            } else if (type.equals("5")) {
                List<String> list = new ArrayList<>();
                int[][] arr = new int[groupId+1][26];
                
                for (int i=1; i<=N; i++) {
                    int alpha = codes[i-1];
                    int groupI = stArr[alpha].getGroupId(i);
                    arr[groupI][alpha]++;
                }
            
                for (int[] cnt : arr) {
                    StringBuilder sb = new StringBuilder();
                    for (int i = 0; i < 26; i++) {
                        if (cnt[i] > 0) {
                            sb.append((char)('a'+i)).append(" ").append(cnt[i]).append(" ");
                        }
                    }
                    if (sb.length() > 0) {
                        list.add(sb.toString().trim());
                    }
                }
            
                answer.addAll(list);
            }
        }

        return answer.toArray(String[]::new);
    }
    
}