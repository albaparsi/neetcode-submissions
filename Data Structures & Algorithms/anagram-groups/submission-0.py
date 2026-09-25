class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashMaps = []

        for s in strs:
            freq = {}
            for ch in s:
                freq[ch] = 1 + freq.get(ch, 0)
            hashMaps.append(freq)


        groups = []
        visited = set()

        # compare and group
        for i in range(len(hashMaps)):
            if i in visited:
                continue

            group = [strs[i]]
            visited.add(i)

            for j in range(i + 1, len(hashMaps)):
                if j not in visited and hashMaps[i] == hashMaps[j]:
                    group.append(strs[j])
                    visited.add(j)

            groups.append(group)

        return groups

 


        
        