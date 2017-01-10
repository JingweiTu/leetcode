class Solution(object):

    # O(n/1000) time complexity. Linear space complexity.
    # Literally just a chain of if statements. We consider nums 3 digits at a time and 
    # build a string based off those digits and the rules of the English language.
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
        
        output = ""
        place_counter = 0
        place = ["","Thousand", "Million", "Billion", "Trillion"]
        onesDigit = {1: "One", 2: "Two", 3: "Three", 4:"Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine"}
        tensDigit = {10: "Ten", 11:"Eleven", 12: "Twelve", 13: "Thirteen", 14: "Fourteen", 15:"Fifteen", 16: "Sixteen", 17: "Seventeen", 18: "Eighteen", 19: "Nineteen", 20:"Twenty", 30: "Thirty", 40:"Forty", 50:"Fifty", 60:"Sixty",70: "Seventy",80:"Eighty",90:"Ninety"}
        while num != 0:
            if place_counter > 0 and num%1000 != 0:
                output = " " + place[place_counter] + output
                
            tens = num%100
            ones = num%10
            
            if tens == 0:
                pass
            elif tens < 20 and tens > 9:
                output = " " + tensDigit[tens] + output
            elif tens < 10 and tens > 0:
                output = " " + onesDigit[tens] + output
            elif tens >= 20 and ones != 0:
                output = " " + tensDigit[tens - ones] + " " + onesDigit[ones] + output
            else: 
                output = " " + tensDigit[tens - ones] + output
                
            hundreds = (num%1000)//100
            
            if hundreds > 0:
                output = " " + onesDigit[hundreds] + " Hundred" + output
            
            place_counter += 1
            num = num//1000
            
        return output[1:len(output)]
        
        