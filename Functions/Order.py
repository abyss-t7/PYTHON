def deploy(image, tag, replicas , region):
    print(f"Deploying {image}:{tag} x{replicas} at {region}")
    
deploy("Nginx", 4, "v.12", "cloud")

deploy(region="cloud", tag=6, replicas="v:14", image="myapp")