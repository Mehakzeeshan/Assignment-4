C :float  = 299792458  # speed of light in m/s

mass_in_kg = float(input("Enter mass in kg: "))

energy_in_joules = mass_in_kg * C ** 2

print(f"C = {C}m/s")
print(f"mass = {mass_in_kg}kg")
print(f"\n Energy in Joules = mc^2")
print(f"\nEnergy = {energy_in_joules} Joules")
