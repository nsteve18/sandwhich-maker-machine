"""
Ham Sandwich Maker Machine
Interactive Python terminal application that handles sandwich orders,
resource management, and coin processing.
"""

# Initial inventory resources
resources = {
    "bread": 12,  # slices
    "ham": 18,    # slices
    "cheese": 24  # ounces
}

# Recipe definitions and prices
recipes = {
    "small": {
        "ingredients": {
            "bread": 2,
            "ham": 4,
            "cheese": 4,
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,
            "ham": 6,
            "cheese": 8,
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,
            "ham": 8,
            "cheese": 12,
        },
        "cost": 5.5,
    }
}


class SandwichMachine:
    def __init__(self, resources):
        """
        Assigns input resources to the machine_resources attribute.
        """
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """
        Returns True when order can be made, False if ingredients are insufficient.
        """
        for item, amount in ingredients.items():
            if self.machine_resources.get(item, 0) < amount:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        """
        Prompts user for coins and returns the total calculated from coins inserted.
        """
        print("Please insert coins.")
        large_dollars = int(input("how many large dollars?: "))
        half_dollars = int(input("how many half dollars?: "))
        quarters = int(input("how many quarters?: "))
        nickels = int(input("how many nickels?: "))

        total = (large_dollars * 1.00) + (half_dollars * 0.50) + (quarters * 0.25) + (nickels * 0.05)
        return round(total, 2)

    def transaction_result(self, coins, cost):
        """
        Returns True when the payment is accepted, or False if money is insufficient.
        """
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deducts required ingredients from resources and prints a confirmation message.
        """
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")

### Make an instance of SandwichMachine class and write the rest of the codes ###
def main():
    sandwich_maker = SandwichMachine(resources)
    is_on = True

    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker.machine_resources['cheese']} pound(s)")
        elif choice in recipes:
            sandwich_type = recipes[choice]
            if sandwich_maker.check_resources(sandwich_type["ingredients"]):
                coins_inserted = sandwich_maker.process_coins()
                if sandwich_maker.transaction_result(coins_inserted, sandwich_type["cost"]):
                    sandwich_maker.make_sandwich(choice, sandwich_type["ingredients"])
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()