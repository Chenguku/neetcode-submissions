class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + str(len(string)) + '/' + string
        print(encoded)
        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        num = ""
        i = 0
        while i < len(s):
            if s[i].isdigit():
                num = num + s[i]
                i = i + 1
            elif s[i] == '/':
                length = int(num)
                arr.append(s[i + 1:i + length + 1])
                num = ""
                i = i + length + 1
        return arr