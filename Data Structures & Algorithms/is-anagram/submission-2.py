class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        self.charRegistryForT = [0] * 26  
        self.charRegistryForS = [0] * 26  
        if len(s) != len(t):
            return False
        for i in range(0, len(s)):
            currentIndexForS = ord(s[i]) - 97
            currentIndexForT = ord(t[i]) - 97
            self.charRegistryForT[currentIndexForS] += 1
            self.charRegistryForS[currentIndexForT] += 1
        #print(self.charRegistry)
        return self.charRegistryForS == self.charRegistryForT