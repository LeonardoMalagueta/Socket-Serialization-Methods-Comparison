# Socket-Dispatch-Methods-Comparison

Implementation of three different message dispatch methods over TCP sockets, focusing on comparing performance, packet size, and message structure.

*by Leonardo de Freitas*

---

## How to run

### **Prerequisites**

1. Make sure the TCP server is running and accepting connections.
2. Tests were performed in a local environment, but any network that allows direct client–server communication works.
3. If something goes wrong, check your machine’s IP using `ipconfig` (Windows) or `ifconfig` (Linux/macOS).

---

### **Running the Methods**

Inside the `./dist` directory, you will find three executable clients:

- `AclientString.exe`  
- `AlientJson.exe`  
- `AlientProto.exe`

Each client sends the same set of operations (**Auth**, **Echo**, **Sum**, and many other queries) but using different message formats (String, JSON, and Protobuffers).

#### **Steps**
1. Open a terminal inside the `/dist` folder.
2. Double-click the executable programs

   or
   
2. Run any of the clients:

```bash
./AclientString.exe
./AclientJson.exe
./AclientProto.exe
