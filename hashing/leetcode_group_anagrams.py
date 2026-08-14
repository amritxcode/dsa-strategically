class Solution:
    def group_anagrams(self,strs:str)-> list:
        groups = {}

        for word in strs:
            key = "".join(sorted(word))

            if key not in groups:
                groups[key] = []

            groups[key].append(word)

        return list(groups.values())

strs = input().split()

print(Solution().group_anagrams(strs))