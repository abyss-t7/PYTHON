def log(*messages):
    for msg in messages:
        print(f"[LOG] {msg}")

log("Server started")
log("Connected", "Port 8080", "Secure mode ON")
log("Deploy started", "Image pulled", "Container running", "Health check passed")