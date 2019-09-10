class Solution {
public:
    string convertToTitle(int n) {
        
        string arr = "ZABCDEFGHIJKLMNOPQRSTUVWXY";
        int num = n, rem;
        string ans;
        while( num > 0)
        {
            rem = num%26;
            if( rem == 0)
                num = (num/26) - 1;
            else
                num /= 26;
            ans.push_back(arr[rem]);
            
        }
        
        std::reverse(std::begin(ans), std::end(ans));
        
        return ans;
    }
};