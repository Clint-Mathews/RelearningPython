class Solution:
    def isValidSimple(self, s: str) -> bool:
        if len(s) % 2 == 1: return False
        result = []
        matchPair = {
            '}':'{',
            ')': '(',
            ']': '[',
        }
        for character in s:
            if character in "[,{,(".split(','):
                result.append(character)
            else:
                if len(result) == 0 or matchPair[character] != result.pop():
                    return False
        return len(result) == 0


if __name__=='__main__':
    sol = Solution()
    res = sol.isValidSimple(")")
    print(res)