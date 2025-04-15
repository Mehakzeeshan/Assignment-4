degree_fahrenheit = input ('Enter temperature in Fahrenheit: ')
degree_fahrenheit = float(degree_fahrenheit)

degree_celsius = float(degree_fahrenheit - 32) * 5.0 / 9.0

print(f"Temperature: {degree_fahrenheit} = \033[1;3m{degree_celsius}C\033[0m")