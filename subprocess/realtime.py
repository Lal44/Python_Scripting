import subprocess
process = subprocess.Popen(["ping", "-c", "3", "google.com"], stdout=subprocess.PIPE, text=True)
for line in process.stdout:
    print(line.strip())