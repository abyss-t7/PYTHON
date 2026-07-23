k = open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O//kimi.txt", "w")
k.write("Never betrays the loyal friend !\n")
k.write("One day we all will die !\n")

k = open("/mnt/8c04d511-6bcd-4d60-8be1-5ea58b6e4015/5 Goal_Dream_Aim/PYTHON/File I-O//kimi.txt", "r")
content = k.read()
print(content)
k.close()

"""In Python, when you open a file with "w", the file pointer is strictly set up for writing
 only. It cannot read. If you try to call .read() on a write-only file object, Python will 
 throw an io.UnsupportedOperation: not readable error.
 So we have to open a file in read "r" mood to print the content inside the kimi.txt."""