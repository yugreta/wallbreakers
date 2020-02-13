class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s: # if empty string
            return True
        
        upr_s = s.upper()
        front_ptr = 0
        back_ptr = len(s)-1
        
        while front_ptr != back_ptr:
            while front_ptr!=back_ptr and (48>ord(upr_s[front_ptr]) or 57<ord(upr_s[front_ptr])<65 or 90<ord(upr_s[front_ptr])): # not alphanum
                front_ptr += 1
            while front_ptr!=back_ptr and (48>ord(upr_s[back_ptr]) or 57<ord(upr_s[back_ptr])<65 or 90<ord(upr_s[back_ptr])):
                back_ptr -= 1
            if front_ptr != back_ptr:
                if upr_s[front_ptr] != upr_s[back_ptr]:
                    return False
                elif back_ptr == front_ptr+1:
                    return True
                else:
                    front_ptr += 1
                    back_ptr -= 1
            
        return True
