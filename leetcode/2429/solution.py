class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        b1 = self.convertToBinaryList(num1)
        b2 = self.convertToBinaryList(num2)

        ansInBinary = [0 for _ in range(max(len(b2), len(b1)))]
        bitsToSet = sum(b2)
        setBits = 0
        for i in range(len(b1) -1, -1, -1):
            if setBits < bitsToSet and b1[i] == 1:
                ansInBinary[i] = 1
                setBits += 1
        
        i = 0
        while setBits < bitsToSet:
            if ansInBinary[i] == 0:
                ansInBinary[i] = 1
                setBits += 1
            i += 1

        ans = 0
        ansInBinary.reverse()
        for bit in ansInBinary:
            ans = (ans << 1) | bit
        return ans
                    
    def convertToBinaryList(self, n):
        ans = []
        while n > 0:
            ans.append(n % 2)
            n = n // 2
        return ans





# 1. binary representation of num1 and num2
# 2. count set bits in num2
# 3. match as many set bits as we can to num1
# 4. set remaining set bits, starting from the left



#  num1 = 1, num2 = 12
#  n1: 0001 n2:1100


        