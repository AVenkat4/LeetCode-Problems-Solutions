class Solution {
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
     
        int n = nums.size();
        int zero = 0;
        unordered_map<int, int> indMap;
        vector< vector<int> > result;
        
        sort(nums.begin(), nums.end());
        
        for(int i = 0; i < n-1; i++)
        {
            if(nums[i] > 0)
                break;
            if(i == 0 || (i > 0 && nums[i] != nums[i-1])){
                int lo = i+1, hi = n-1, sum = 0 - nums[i];
                while(lo < hi){
                    if(nums[lo] + nums[hi] == sum){
                        vector<int> triple;
                        triple.push_back(nums[i]), triple.push_back(nums[lo]), triple.push_back(nums[hi]);
                        result.push_back(triple);
                        while(lo < hi && nums[lo] == nums[lo + 1]) lo++;
                        while(lo < hi && nums[hi] == nums[hi - 1]) hi--;
                        lo++;
                        hi--;
                    }
                    else if(nums[lo] + nums[hi] < sum){
                        while(lo < hi && nums[lo] == nums[lo + 1]) lo++;
                        lo++;
                    }
                    else{
                        while(lo < hi && nums[hi] == nums[hi - 1]) hi--;
                        hi--;
                    }
                }
                
            }
        }
        
        return result;
    }
};