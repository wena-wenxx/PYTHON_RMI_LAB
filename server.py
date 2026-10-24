import Pyro5.api
from product import Product

HOST = "127.0.0.1"   
PORT = 9000          


# ---------- ProductImpl.java ----------
@Pyro5.api.expose    
class ProductImpl(Product):
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def getName(self):
        print(f"[server] getName() called on {self.name}")
        return self.name

    def getDescription(self):
        print(f"[server] getDescription() called on {self.name}")
        return self.description

    def getPrice(self):
        print(f"[server] getPrice() called on {self.name}")
        return self.price


# ---------- Server.java ----------
def main():
    print("Server is booting....")

    p1 = ProductImpl("Laptop", "Lenovo laptop", 800000.0)
    p2 = ProductImpl("Mobile", "MI 9 mobile", 24000.0)
    p3 = ProductImpl("Bag", "Branded bag", 800.0)
    p4 = ProductImpl("Charger", "MI Charger", 230.0)

    daemon = Pyro5.api.Daemon(host=HOST, port=PORT)

    objects = {"laptop": p1, "ram": p2, "bag": p3, "charger": p4}
    for name, obj in objects.items():
        uri = daemon.register(obj, objectId=name)
        print(f"Registered '{name}' at {uri}")

    print(f"Server is ready on {HOST}:{PORT}. Press Ctrl+C to stop.")
    daemon.requestLoop()   

if __name__ == "__main__":
    main()
