class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        
        unordered_map<int, int> m;
        int n = arr.size();
        for(int i = 0; i < n; i++)
        {
            if(!m.count(arr[i]))
                m[arr[i]] = 0;
            m[arr[i]] += 1;
        }
        
        unordered_map<int, int> c;
        unordered_map<int, int>::iterator it;
        for(it = m.begin(); it!= m.end(); it++)
        {
            if(c.count(it -> second))
            {   return false;
                c[it->second] = 0;
            }
            
            c[it->second] += 1;
        }
        
        return true;
    }
};