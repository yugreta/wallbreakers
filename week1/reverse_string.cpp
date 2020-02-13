class Solution {
public:
    void reverseString(vector<char>& s) {
        char temp;
        
        int back_i = s.size()-1;
        for (int i = 0; i<s.size()/2; ++i) {
            temp = s[i];
            s[i] = s[back_i];
            s[back_i] = temp;
            --back_i;
        }
    }
};