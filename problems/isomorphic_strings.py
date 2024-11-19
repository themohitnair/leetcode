from typing import Dict, Set

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        char_map1: Dict[str, Set[str]] = {}
        char_map2: Dict[str, Set[str]] = {}
        if len(s) != len(t):
            return False
        for s_char, t_char in zip(s, t):
            if s_char in char_map1:
                char_map1[s_char].add(t_char)
            else:
                char_map1[s_char] = {t_char}
        for t_char, s_char in zip(t, s):
            if t_char in char_map2:
                char_map2[t_char].add(s_char)
            else:
                char_map2[t_char] = {s_char}
        for v in char_map1.values():
            if len(v) > 1:
                return False
        for v in char_map2.values():
            if len(v) > 1:
                return False
        return True