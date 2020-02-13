class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs: # check if array is empty
            return ""
        
        prefix = strs[0]
        if len(strs)>1:
            for word in strs[1:]:
                prefix = prefix[:min(len(prefix), len(word))]
                for i in range(len(prefix)):
                    if prefix[i] != word[i]:
                        if i==0:
                            return ""
                        prefix = prefix[:i]
                        break
                        
        return prefix
