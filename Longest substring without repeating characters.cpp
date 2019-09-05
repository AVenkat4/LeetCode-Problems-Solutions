class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        
        int arr[256];
        if(s.size() <= 1)
            return s.size();
        memset(arr, -1, sizeof(arr));
        int start_index = 0, largest = INT_MIN;
        for(int i = 0; i < s.size(); i++)
        {
            if(arr[s[i]] == -1)
            {
                arr[s[i]] = i;
            }
            else
            {
                if( arr[s[i]] + 1 > start_index)
                    start_index = arr[s[i]] + 1;
                arr[s[i]] = i;
            }
            //cout << endl << start_index <<" " << i;
            largest = max(largest, i - start_index + 1);
        }
        
        return largest;
    }
};