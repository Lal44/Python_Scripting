import subprocess
output = subprocess.run(["echo" , "hellow"], text=True, capture_output = True)
print(output.returncode)