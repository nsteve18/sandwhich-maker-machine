import data
import sandwich_maker
import cashier

# Assign data variables from module
resources = data.resources
recipes = data.recipes

# Instantiate class objects
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()


def main():
    is_on = True

    while is_on:
        choice = input("What would you like? (small/ medium/ large/ off/ report): ").strip().lower()

        if choice == "off":
            is_on = False
        elif choice == "report":
            print(f"Bread: {sandwich_maker_instance.machine_resources['bread']} slice(s)")
            print(f"Ham: {sandwich_maker_instance.machine_resources['ham']} slice(s)")
            print(f"Cheese: {sandwich_maker_instance.machine_resources['cheese']} pound(s)")
        elif choice in recipes:
            sandwich_type = recipes[choice]
            if sandwich_maker_instance.check_resources(sandwich_type["ingredients"]):
                coins_inserted = cashier_instance.process_coins()
                if cashier_instance.transaction_result(coins_inserted, sandwich_type["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich_type["ingredients"])
        else:
            print("Invalid selection. Please try again.")


if __name__ == "__main__":
    main()