class Solution(object):

    # Naive solution. 
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        output = 0
        tens_power = 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        carry = 0
        for i in range(max(len(num1),len(num2))):
            if len(num1) > i and len(num2) > i: 
                output += ((int(num1[i]) + int(num2[i]) + carry)%10)*10**tens_power
                carry = (int(num1[i]) + int(num2[i]) + carry)//10
                tens_power += 1
                # print(1,output)
            elif (len(num1) > i and len(num2) <= i):
                output += ((int(num1[i]) + carry)%10)*10**tens_power
                carry = (int(num1[i]) + carry)//10
                tens_power += 1
                # print(2,output)
            elif (len(num2) > i and len(num1) <= i):
                output += ((int(num2[i])+ carry)%10)*10**tens_power
                carry = (int(num2[i]) + carry)//10
                tens_power += 1
                # print(3,output)

        output += carry*10**tens_power
            
        return str(output)
