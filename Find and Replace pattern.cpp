class Solution {
public:
    
    string toPattern(string pat)
    {
        int count = 0;
        int plen = pat.length();
        unordered_map<char, char> m;
        
        for(int i = 0; i < plen; i++)
            if( !m.count(pat[i]) )    
                m[pat[i]] = char(count++);
        
        string s;
        for(int i = 0; i < plen; i++)
            s += (m[pat[i]]);
        
        return s;
    }
    
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        
        string p = toPattern(pattern);
        int num = words.size();
        string w;
        vector<string> result;
        for(int i = 0; i < num; i++)
        {
            w = toPattern(words[i]);
            if( w == p )
                result.push_back(words[i]);
        }
        
        return result;
    }
};