import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind(('localhost', 8888))

servidor.listen()
cliente, end = servidor.accept()

Terminado = False
Duvida = True

while not Terminado:

  msg = cliente.recv(1024).decode('utf-8')
  if msg == 'finalizar':
    terminado = True
  if msg == 'FINALIZAR':
    Terminado = True
  if msg == 'Finalizar':
    Terminado = True
  else:
    print(msg)
  cliente.send(input('Mensagem: ').encode('utf-8'))


while not Duvida:

   msg = cliente.recv(1024).decode('utf-8')
   if msg == 'sim':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
   if msg == 'SIM':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
   if msg == 'Sim':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
   else:
    print(msg)

cliente.close()
servidor.close()

  