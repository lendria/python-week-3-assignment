def calculate_discount(price, discount_percent):
    # Convert discount percent to float
    discount_percent = float(discount_percent)
    
    # Check if discount is 20% or higher
    if discount_percent >= 20:
        # Apply discount
        final_price = price * (1 - discount_percent / 100)
    else:
        # No discount applied
        final_price = price
    
    return final_price

# Main script
while True:
    try:
        original_price = float(input("Enter the original price: "))
        discount_percent = float(input("Enter the discount percentage (in %): "))

        final_price = calculate_discount(original_price, discount_percent)
        
        print(f"The final price after applying the discount is: ${final_price:.2f}")
        
        cont = input("Do you want to continue? (y/n): ")
        if cont.lower() != 'y':
            break
    except ValueError:
        print("Invalid input. Please enter valid numbers.")
