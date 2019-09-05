class Solution {
public:
    string removeDuplicateLetters(string text) {
        
        int n = text.size();
        int arr[256] = {0};
        
        for(int i = 0; i < n; i++)
            arr[text[i]]++;
        
        int visited[256] = {0};
        string result = "0";
        for(int i = 0; i < n; i++)
        {
            arr[text[i]]--;
            if(visited[text[i]])
                continue;
            
            while(result.back() > text[i] && arr[result.back()])
            {   visited[result.back()] = 0; 
                result.pop_back();
            }
            
            result += text[i];
            visited[text[i]] = 1;
        }
        
        
        return result.substr(1);
    }
};