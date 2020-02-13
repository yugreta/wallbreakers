class Solution {
public:
    string reverseWords(string s) {
        int front = 0;
        int next = 1;
        int back = s.size();
        int swap_i;
        
        while (front<back) {
            while (next!=back && s[next]!=' ') {
                ++next;
            }
            
            if (front+1!=next) {
                swap_i = next-1;
                int middle = (front+next)/2;
                while (front!=middle) {
                    char temp = s[front];
                    s[front] = s[swap_i];
                    s[swap_i] = temp;
                    ++front;
                    --swap_i;
                }
            }
            ++next;
            front = next;
        }
        
        return s;
    }
};