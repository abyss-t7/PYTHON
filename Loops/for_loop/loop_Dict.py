config = {"host": "localhost", "port": 8080, "debug": True}

for key in config: # mere key 
    print(key)
    
print("== mere values  ==")
    
for val in config.values(): # mere values 
    print(val)
    
print("== both key and values ==")

for key, val in config.items(): # both key and values
    print(f"{key} = {val}")