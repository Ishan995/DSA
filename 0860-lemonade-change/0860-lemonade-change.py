class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        n=len(bills)
        five=0
        ten=0
        for i in range(n):
            money=bills[i]
            if money==5:
                five+=1
            elif money==10:
                if five==0:
                    return False
                five-=1
                ten+=1
            elif money==20:
                if ten>0:
                    ten-=1
                    if five==0:
                        return False
                    five-=1
                else:
                    if five<3:
                        return False
                    five-=3
        return True

        