class Solution:
    def isAlternate(self, choppedlist: List[int])-> bool:
        for i in range (len(choppedlist)-1):
            if(choppedlist[i] == choppedlist[i+1]):
                return False
        return True

    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        altergroups = 0
        lengthoflist=len(colors)

        for startpoint in range (lengthoflist-k+1):
            choppedlist = colors[startpoint:startpoint+k]
            if(self.isAlternate(choppedlist)):
                altergroups+=1

        for startpoint2 in range(lengthoflist-k+1, lengthoflist):
            choppedlist2 = colors[startpoint2: lengthoflist]
            r= len(choppedlist2)
            a = k-r #len(resofthelsit)
            reastofthelist = colors[:a]
            rotatinglist = choppedlist2 + restofthelist
            print(rotatinglist)
            if(self.isAlternate(rotatinglist)):
                altergroups+=1
        return altergroups  

        