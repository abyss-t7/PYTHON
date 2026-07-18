def connect(host="local", port=8080, secure=False):
    print(f"Connecting to {host} at port{port} which is secure={secure}")
    
connect("Localhost")
connect("localhost", 8080, True)
    