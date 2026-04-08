class Solution(object):
    def __init__(self, word1, word2):  # Pass args or use input inside method
        self.word1 = word1
        self.word2 = word2
        self.merged = []  # Initialize empty list

    def merge(self):
        max_len = max(len(self.word1), len(self.word2))
        for i in range(max_len):
            if i < len(self.word1):
                self.merged.append(self.word1[i])
            if i < len(self.word2):
                self.merged.append(self.word2[i])
        return ''.join(self.merged)  # Return string result

# Usage (interactive inputs)
# Creating Multiple Objects
word1 = input("Enter word1: ")
word2 = input("Enter word2: ")
merged_word = Solution(word1, word2)
print(merged_word.merge())
