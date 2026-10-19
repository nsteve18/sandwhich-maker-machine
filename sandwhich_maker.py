class SandwichMaker:
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

    def make_sandwich(self, sandwich_size, order_ingredients):
        """
        Deducts required ingredients from resources and prints a confirmation message.
        """
        for item, amount in order_ingredients.items():
            self.machine_resources[item] -= amount
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")