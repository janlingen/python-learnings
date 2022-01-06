class Inventory:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.items = {}
        self.item_count = 0

    def add_item(self, name, price, quantity):
        if self.item_count+quantity > self.max_capacity or name in self.items:
            return False
        self.item_count += quantity
        self.items[name] = [name, price, quantity]
        return True

    def delete_item(self, name):
        if name not in self.items:
            return False
        self.item_count -= self.items[name][2]
        del self.items[name]
        return True

    def get_items_in_price_range(self, min_price, max_price):
        lst = []
        for item in self.items.values():
            if min_price <= item[1] <= max_price:
                lst.append(item[0])
        return lst

    def get_most_stocked_item(self):
        max_item_name = None
        max_quant = 0
        if self.item_count > 0:
            for item in self.items.values():
                if max_quant < item[2]:
                    max_item_name = item[0]
                    max_quant = item[2]
        return max_item_name
