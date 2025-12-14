import subprocess
result = subprocess.run(["ls", "/nonexistent"], capture_output=True, text=True)
print("STDOUT:", result.stdout)
print("STDERR:", result.stderr)