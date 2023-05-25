# Variáveis
tempCelsius = float(input("Digite a temperatura em Celsius: "))

# Funções
def transformar_Fahrenheit(tempC):
    tempF = (9 * tempC + 160)/5
    return tempF

tempFahrenheit = transformar_Fahrenheit(tempCelsius)

print("A tempertaura", tempCelsius, "ºC, em Fahrenheit é:", tempFahrenheit, "ºF.")