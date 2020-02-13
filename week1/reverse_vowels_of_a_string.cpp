class Solution {
public:
    string reverseVowels(string s) {
        int front = 0;
        int back = s.size()-1;
        int temp;
        
        while (front<back) {
            while (s[front]!='a' && s[front]!='e' && s[front]!='i' && s[front]!='o' && s[front]!='u' && s[front]!='A' && s[front]!='E' && s[front]!='I' && s[front]!='O' && s[front]!='U' && front<back) {
                ++front;
            }
            while (s[back]!='a' && s[back]!='e' && s[back]!='i' && s[back]!='o' && s[back]!='u' && s[back]!='A' && s[back]!='E' && s[back]!='I' && s[back]!='O' && s[back]!='U' && front<back) {
                --back;
            }
        
            if (front<back) {
                temp = s[front];
                s[front] = s[back];
                s[back] = temp;
                if (front+1==back) {
                    break;
                }
                front += 1;
                back -= 1;
            }
        }
        
        return s;
    }
};