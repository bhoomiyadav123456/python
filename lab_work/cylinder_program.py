from three_d_figures import cylinder_csa, cylinder_tsa, cylinder_volume

r = float(input("Enter radius: "))
h = float(input("Enter height: "))

print("Curved Surface Area = - cylinder_program.py:6", cylinder_csa(r, h))
print("Total Surface Area = - cylinder_program.py:7", cylinder_tsa(r, h))
print("Volume = - cylinder_program.py:8", cylinder_volume(r, h))