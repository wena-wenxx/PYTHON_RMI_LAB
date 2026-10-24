# Python RMI Lab (Pyro5)

This project translates the Java RMI project
[JAVA_RMI_IV](https://github.com/nix1947/sunway_dpp/tree/master/JAVA_RMI_IV)
into Python using **Pyro5** (Python Remote Objects).

## Files

| Python file  | Java equivalent                                   | What it does                                   |
|--------------|---------------------------------------------------|------------------------------------------------|
| `product.py` | `Product.java`                                    | The remote interface: `getName()`, `getDescription()`, `getPrice()` |
| `server.py`  | `ProductImpl.java`, `Server.java`, `ServerImpl.java` | Creates 4 products and shares them on `127.0.0.1:9000` |
| `client.py`  | `Client.java`                                     | Connects to the server and prints each product |

## How Java RMI maps to Pyro5

| Java RMI                                   | Pyro5                                   |
|--------------------------------------------|-----------------------------------------|
| `interface Product extends Remote`         | `class Product(ABC)` in `product.py`    |
| `UnicastRemoteObject.exportObject(p1, 0)`  | `@Pyro5.api.expose` + `daemon.register()` |
| `LocateRegistry.getRegistry(host, 9000)`   | `Pyro5.api.Daemon(host, port=9000)`     |
| `registry.bind("laptop", stub)`            | `daemon.register(p1, objectId="laptop")` |
| `registry.lookup("laptop")`                | `Pyro5.api.Proxy("PYRO:laptop@127.0.0.1:9000")` |

## Requirements

- Python 3.8 or newer
- Pyro5

```bash
pip install Pyro5
```

## How to run

You need **two terminals**, both opened inside this folder.

**Terminal 1 – start the server first:**

```bash
python server.py
```

Wait until you see `Server is ready on 127.0.0.1:9000`. Leave it running.

**Terminal 2 – run the client:**

```bash
python client.py
```

The client prints the name, description and price of the Laptop, Mobile, Bag and Charger.
The server terminal shows which methods the client called.

Stop the server with **Ctrl + C**.

## Sample output

Client:
```
Name: Laptop
Description: Lenovo laptop
Price: 800000.0
------------------------------
...
```

Server:
```
Server is booting....
Registered 'laptop' at PYRO:laptop@127.0.0.1:9000
...
Server is ready on 127.0.0.1:9000. Press Ctrl+C to stop.
[server] getName() called on Laptop
```
