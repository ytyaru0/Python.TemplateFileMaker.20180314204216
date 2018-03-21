import subprocess
p = subprocess.Popen('ls', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout_data, stderr_data = p.communicate()
print(stdout_data.decode('UTF-8'))
print(stderr_data.decode('UTF-8'))
