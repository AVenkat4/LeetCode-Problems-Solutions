class Solution {
public:
    int toNum(string s)
    {
        int n = s.length();
        int num = 0;
        for(int i = 0; i < n; i++)
            num += (int(s[n - i - 1])-48)*pow(10, i);
        
        return num;
    }
    
    string flip(string s)
    {
        int n = s.length();
        int left = 0, right = n-1;
        while( left < right)
            s[right--] = s[left++];
        
        return s;
    }
    string nearestPalindromic(string s) {
        
        int n = s.size();
        set<long> candidates;
        candidates.insert(pow(10, n-1) - 1);
        candidates.insert(pow(10, n-1) + 1);
        candidates.insert(pow(10, n) - 1);
        candidates.insert(pow(10, n) + 1);
        
        long prefix = stol(s.substr(0, (n+1)/2));
        string candidate_pal;
        for(int i = -1; i <= 1; i++)
        {
            long p = prefix + i;
            candidate_pal = to_string(p);
            string rev_cpal(candidate_pal.rbegin(), candidate_pal.rend());
            if( n % 2) //odd
                candidate_pal += rev_cpal.substr(1, rev_cpal.size()-1);
            else
                candidate_pal += rev_cpal;
            
            candidates.insert(stol(candidate_pal));
        }
        
        long min_pal = LONG_MAX, min_dis = LONG_MAX;
        long num = stol(s), pal;
        candidates.erase(num);
        for(set<long>::iterator i = candidates.begin(); i != candidates.end(); i++)
        {
            pal = *i;
            if(min_dis > fabs(pal - num) )
            {   min_pal = pal;    
                min_dis = fabs(pal - num);
            }
            else if(min_dis == fabs(pal - num))
                min_pal = min(min_pal, pal);
            
        }
        
        return to_string(min_pal);
    }
};