# Convert meters into differents unitis of measure

x = float(input('Type the distance in meters: '))

km = x / 1000
cm = x * 100
mm = x *1000

print('\n{} meters\n{} kilometers\n{}centimeters\n{} milimeters'.format(x, km, cm, mm))