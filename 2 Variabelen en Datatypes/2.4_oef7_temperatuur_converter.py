temperatuur_fahrenheit = input("Geef een temperatuur in Fahrenheit in: ")
temperatuur_fahrenheit = float(temperatuur_fahrenheit)

temperatuur_celsius = (temperatuur_fahrenheit - 32) * 5 / 9

print(f"{temperatuur_fahrenheit}°F is gelijk aan {temperatuur_celsius:.1f}°C")
