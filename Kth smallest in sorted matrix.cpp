class Tuple
{
    public:
    int x, y, val;
    Tuple(int row = 0, int col = 0, int value = 0):x(row), y(col), val(value){}
};

bool operator<(const Tuple& t1, const Tuple& t2)
{
    return t1.val > t2.val;
}
class Solution {
public:
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        
        int n = matrix.size();
        priority_queue<Tuple> pq;
        Tuple t;
        int row, col;
        for(int i = 0; i < n; i++)
        {   pq.push(Tuple(0, i, matrix[0][i])); }
        
        for(int j = 0; j < k-1; j++)
        {
            t = pq.top();
            row = t.x + 1;
            col = t.y;
            pq.pop();
            if(t.x == n-1)
                continue;
            //cout << row-1 << " " << col << matrix[row-1][col] << endl;
            pq.push(Tuple(row, col, matrix[row][col]));
        }
        
        t = pq.top();
        return t.val;
    }
};