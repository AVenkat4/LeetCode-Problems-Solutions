class Solution {
public:
    int getMin(vector<int> arr, int low, int high)
    {
        if( low > high )
            return -1;
        if( low == high )
            return low;
        int mid;
        while(low <= high)
        {
            mid = low + (high - low)/2;
            if(mid < high && arr[mid] > arr[mid + 1])
                return mid + 1;
            
            if(mid > low && arr[mid] < arr[mid - 1])
                return mid;
            
            if(arr[low] >= arr[mid])
                high = mid-1;
            else
                low = mid + 1;
            
        }
        
        return 0;
    }
    
    int findMin(vector<int>& nums) {
        
        int pos = getMin(nums, 0, nums.size()-1);
    
        return nums[pos];
    }
};