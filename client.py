import Pyro5.api

HOST = "127.0.0.1"
PORT = 9000


def show(name):
    uri = f"PYRO:{name}@{HOST}:{PORT}"
    with Pyro5.api.Proxy(uri) as product:
        print("Name:", product.getName())
        print("Description:", product.getDescription())
        print("Price:", product.getPrice())
        print("-" * 30)


def main():
    try:
        for name in ["laptop", "ram", "bag", "charger"]:
            show(name)
    except Exception as e:
        print("Exception in client side:", e)


if __name__ == "__main__":
    main()
