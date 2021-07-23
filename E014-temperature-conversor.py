# Convert celsius to fahrenheit or fahrenheit to celsius

tempFormat = int(input("What is the unit of temperature? Type (1) for Celsius or (2) for Fahrenheit."))
tempValue = float(input('Type the value of the temperature: '))

if tempFormat == 2:
    tempOutput = (tempValue - 32) / 1.8
    print('{:.2f} Fahrenheit is {:.2f} Celsius'.format(tempValue, tempOutput))
if tempFormat == 1:
    tempOutput = (tempValue * 1.8) + 32
    print('{:.2f} Celsius is {:.2f} Fahrenheit'.format(tempValue, tempOutput))
