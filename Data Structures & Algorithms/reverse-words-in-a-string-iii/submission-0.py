class Solution:
    def reverseWords(self, s: str) -> str:
        result = []
        i = 0
        n = len(s)

        while i < n:
            if s[i] == " ":
                result.append(" ")          # Preserve the space
                i += 1
            else:
                start = i                   # Remember the word's start

                while i < n and s[i] != " ": # Stop at a space or the end
                    i += 1

                result.append(s[start:i][::-1])  # Reverse this word only

        return "".join(result)