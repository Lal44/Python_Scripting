import subprocess
try:
    output = subprocess.run(["top"], check=True)
    print("comannd succed")
except subprocess.CalledProcessError:
    print("command failed")