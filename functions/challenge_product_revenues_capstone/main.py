# Définir la fonction calculate_revenue(prices, quantities_sold)
def calculate_revenue(prices, quantities_sold):
    revenue = []
    for price, qty in zip(prices, quantities_sold):
        revenue.append(price * qty)    
    return revenue
# Définir la fonction formatted_output(products, revenues)
def formatted_output(products, revenues):
    revenue_per_product = []
    # Boucles sur products et revenues
    for product, revenue in zip(products, revenues):
        revenue_per_product.append(f"{product} has total revenue of ${revenue}")
        # Trier la liste `revenue_per_product` par ordre alphabétique des noms de produits
    for line in sorted(revenue_per_product):
        print(line)
# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold
# Calculer le chifrre d'affaire par produit dans une liste appelée revenue
revenue = calculate_revenue(prices, quantities_sold)
# Utiliser la fonction zip  pour combiner les listes products et revenue  en une liste de tupples
formatted_output(products, revenue)

