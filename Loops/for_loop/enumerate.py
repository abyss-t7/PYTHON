task = ["build", "test", "deploy", "notify"]
for i, task in enumerate(task, start=1):
    print(f"Step {i}: {task}")
    
    
error = ["ok", "fail", "ok", "fail", "ok"]
failed_at = [i for i, status in enumerate(error) if status == "fail"]
print(failed_at)
