from three_d_figures import cone_csa, cone_tsa, cone_volume
import math

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

l = math.sqrt(r*r + h*h)   # Slant height

print("Curved Surface Area = - cone_program.py:9", cone_csa(r, l))
print("Total Surface Area = - cone_program.py:10", cone_tsa(r, l))
print("Volume = - cone_program.py:11", cone_volume(r, h))