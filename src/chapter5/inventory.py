class Inventory:
    default = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
    def __init__(self, inventory=default):
        self.inventory = inventory

    def display(self):
        s = "Inventory:\n"
        total = 0
        for k, v in self.inventory.items():
            s += f"{v} {k}\n"
            total += v
        s += f"Total: {total}"
        return s

    def add(self, items):
        for i in items:
            self.inventory.setdefault(i, 0)
            self.inventory[i] += 1


i = Inventory()
print(i.display())
dragon_loot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
i.add(dragon_loot)
print(i.display())
