class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        hasm = {}
        for path in paths:
            hasm[path[0]] = path[1]
        for each in hasm.values():
            if each not in hasm.keys():
                return each