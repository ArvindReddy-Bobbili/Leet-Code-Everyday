class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        char_list = list(blocks)
        n = len(char_list)
        minnumberofoperations = []
        sizeofwindow = n - k

        # Check if no operation is needed
        flagvar = self.checkifnooperationneeded(char_list, k)
        if flagvar == 0:
            return 0
        
        # Sliding window logic
        for i in range(sizeofwindow + 1):
            countofW = 0
            countofB = 0
            for a in range(i, i + k):
                if char_list[a] == 'W':
                    countofW += 1
                else:
                    countofB += 1
            minnumberofoperations.append(countofW)
        
        return min(minnumberofoperations)

    def checkifnooperationneeded(self, char_list: list, k: int) -> int:
        countofB = 0
        countofW = 0
        for i in range(len(char_list)):
            if char_list[i] == 'B':
                countofB += 1
                countofW = 0
                if countofB == k:
                    return 0  # No operation needed if we find a window of 'B's
            else:
                countofW += 1
                countofB = 0
        return 1  # Operation needed if we didn't find any window of 'B's
   