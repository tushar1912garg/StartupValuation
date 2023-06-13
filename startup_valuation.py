def calculate_startup_valuation(stage, revenue, growth_rate, industry_multiplier, opportunity_cost, tam, sam, som):
    if stage == 'idea':
        return tam * 0.05
    elif stage == 'prototype':
        return tam * 0.1
    elif stage == 'revenue':
        valuation = revenue * (1 + growth_rate) * industry_multiplier - opportunity_cost
        return valuation * (sam / som)
    else:
        return None

# Prompt the user for input
stage = input("Enter the stage of the startup (idea, prototype, revenue): ")
if stage == 'revenue':
    revenue = float(input("Enter the annual revenue of the startup in dollars: "))
    growth_rate = float(input("Enter the growth rate of the startup (as a decimal): "))
industry_multiplier = float(input("Enter the industry-specific multiplier: "))
opportunity_cost = float(input("Enter the opportunity cost of the founders: "))
tam = float(input("Enter the Total Addressable Market (TAM) of the industry: "))
sam = float(input("Enter the Serviceable Addressable Market (SAM) of the industry: "))
som = float(input("Enter the Serviceable Obtainable Market (SOM) of the industry: "))

# Calculate the startup valuation
valuation = calculate_startup_valuation(stage, revenue, growth_rate, industry_multiplier, opportunity_cost, tam, sam, som)

# Display the result
if valuation is not None:
    print(f"The startup valuation is ${valuation}")
else:
    print("Invalid stage entered. Please choose 'idea', 'prototype', or 'revenue'.")
