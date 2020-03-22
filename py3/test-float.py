multiplierNum1 = 1.69
multiplierNum2 = 1.75
roundLength = 1000000
multiplierResult = multiplierNum1 * multiplierNum2
roundResult = round(multiplierResult*roundLength) / roundLength
print(multiplierResult,roundResult)
