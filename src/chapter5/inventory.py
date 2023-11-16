class Inventory:
    default_inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    def __init__(self, inventory=default_inventory):
        self.inventory = inventory

    def display(self):
        s = "Inventory:\n"
        total = 0
        for k, v in self.inventory.items():
            s += f"{v} {k}\n"
            total += v
        s += f"Total: {total}"
        return s

i = Inventory()
print(i.display())
