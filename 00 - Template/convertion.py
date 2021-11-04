# convertion celcius to other

print("\nConvertion Temp \n")
celcius = float(input('input temp in celcius :'))

print("temp = ", celcius, "C")

#reamur
reamur = (4/5) * celcius
print("temp in reamur = ", reamur, "R")


#fahrenheit
fahrenheit = ((9/5) * celcius) + 32
print("temp in fahrenheit = ", fahrenheit, "F")


#kelvin
kelvin = ((9/5) * celcius) + 32
print("temp in kelvin = ", kelvin, "F")

#fahrenheit to celcius
fahrenheit_celcius = (5/9)  * (celcius - 32)
celcius_kelvin = fahrenheit_celcius + 273
print("fahrenheit to kelvin = ", celcius_kelvin, "CK")