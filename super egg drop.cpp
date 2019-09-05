class Solution {
public:
    int **memo;
    int DP(int k, int n)
    {
        int ans;
        if(memo[k][n] == -1)
        {
            if( n == 0 )
                ans = 0;
            else if( k == 1)
                ans = n;
            else
            {
                int lo = 1;
                int hi = n;
                
                while(lo + 1 < hi)
                {
                    int mid_x = lo + (hi-lo)/2;
                    int t1 = DP(k-1, mid_x-1);
                    int t2 = DP(k, n - mid_x);
                    
                    if( t1 < t2 )
                        lo = mid_x;
                    else if( t2 < t1)
                        hi = mid_x;
                    else
                        lo = hi = mid_x;
                }
                
                int x = lo;
                int ans_lo = max( DP(k-1, x-1), DP(k, n-x) );
                x = hi;
                int ans_hi = max( DP(k-1, x-1), DP(k, n-x) );
                
                ans = 1 + min( ans_lo, ans_hi);
                
            }
            
            memo[k][n] = ans;
        }
        
        return memo[k][n];
    }
    
    int superEggDrop(int K, int N) {
        
        int dp[N+1][K+1] = {0};
        int m = 0;
        
        /*
        for(int i = 0; i <= N; i++)
            for(int j = 0; j <= K; j++)
                dp[i][j] = 0;
        */
        memset(dp, 0, sizeof(dp));
        
        while(dp[m][K] < N)
        {
            m++;
            for(int k = 1; k <= K; k++)
                dp[m][k] = dp[m-1][k-1] + dp[m-1][k] + 1;
        }
        return m;
    }
};