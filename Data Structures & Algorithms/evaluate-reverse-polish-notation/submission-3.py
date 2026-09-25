class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stackBin = []

        for c in tokens:
                
            if c not in ['+','-','/','*']:
                stackBin.append(int(c))

            else:
                    
                operator = c
                operand2 = stackBin.pop()
                operand1 = stackBin.pop()

                if operator == '+' :
                    currentTotal = operand1 + operand2

                elif operator == '-' :
                    currentTotal = operand1 - operand2

                elif operator == '*' :
                    currentTotal = operand1 * operand2

                elif operator == '/' :
                    currentTotal = ((operand1 / operand2))

                stackBin.append(int(currentTotal))

        return int(stackBin[-1])

        