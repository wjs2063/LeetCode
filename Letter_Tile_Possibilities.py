
class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        path = set()
        n = len(tiles)
        answer = 0
        from collections import defaultdict
        table = defaultdict(int)
        # 결국은 주어진 alphabet 으로
        answer = 0
        for tile in tiles:
            table[ord(tile) -  ord('A')] += 1
        def dfs(table):
            result = 0
            for i in range(26):
                # 0~25 사이 알파벳개수
                if table[i] == 0 :
                    continue
                table[i] -= 1
                result += dfs(table) + 1
                table[i] += 1
            return result
        answer = dfs(table)
        return answer
            