
class Queue:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.size() == 0:
            return None
        return self.items.pop(0)

    def show_queue(self):
        print(self.items)


class IceCreamShop:

    def __init__(self, flavors):
        self.flavors = flavors
        self.orders = Queue()

    def take_order(self, customer, flavor, scoops):
        if flavor not in self.flavors:
            print(f"Sorry, {customer}. We're out of {flavor}")
        elif scoops not in range(1, 4):
            print(f"You want {scoops} scoops?")
        else:
            print("Order created!!!")
            order = {"customer": customer, "flavor": flavor, "scoops": scoops}
            self.orders.enqueue(order)

    def show_all_orders(self):
        print("All Pending Ice Cream Orders: ")
        for order in self.orders.items:
            print(
                f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")

    def next_order(self):
        print("Next Order Up!")
        order = self.orders.dequeue()
        # print(order['customer'])
        print(
            f"Customer: {order['customer']} -- Flavor: {order['flavor']} -- Scoops: {order['scoops']}")


shop = IceCreamShop(["rocky road", "mint chip", "pistachio"])
shop.take_order("Zachary", "pistachio", 2)
shop.take_order("Tyler", "rocky road", 2)
shop.show_all_orders()
shop.next_order()
shop.show_all_orders()
