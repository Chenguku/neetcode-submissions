class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in strs:
            encoded = encoded + string + '/'
        return encoded

    def decode(self, s: str) -> List[str]:
        arr = []
        string = ""
        for i in s:
            if i == '/':
                arr.append(string)
                string = ""
            else:
                string = string + i
        return arr