cart = [1200, 1500, 1200, 2000, 1800]

# Remove duplicates
cart = list(set(cart))

total = sum(cart)

# Apply 10% discount
if total > 5000:
    total *= 0.9

# Add GST 18%
total *= 1.18

print("Final Payable Amount: - ecommerce_cart_system.py:15", round(total, 2))

#output:
# Final Payable Amount: - ecommerce_cart_system.py:15 7080.0