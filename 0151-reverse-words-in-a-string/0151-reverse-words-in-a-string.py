class Solution:
    def reverseWords(self, s: str) -> str:
        words=s.split()
        rev_words=words[::-1]
        return " ".join(rev_words)