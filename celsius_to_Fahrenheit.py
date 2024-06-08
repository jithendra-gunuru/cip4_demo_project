#we convert celsius to farenheight

"""
1) we take user input in celsius 
2) convert celsius into fahrenheit (celsius*1.8+32)
3)print farenheit
"""

#helper function
def convert_celsius_to_farenheit():
    celsius = float(input("enter temperature in celsius: "))
    farenheit = (celsius*1.8) + 32
    return farenheit

def main():
    farenheit_temp = convert_celsius_to_farenheit()
    print(farenheit_temp)

if __name__ == "__main__":
    main()