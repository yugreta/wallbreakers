class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        words = str.split()
        
        letter_to_word = {}
        mapped_words = set()
        if len(pattern) == len(words):
            for i in range(len(pattern)):
                if pattern[i] in letter_to_word:
                    if letter_to_word[pattern[i]] != words[i]:
                        return False
                elif words[i] in mapped_words:
                    return False
                else:
                    letter_to_word[pattern[i]] = words[i]
                    mapped_words.add(words[i])
            return True
                    
        return False
