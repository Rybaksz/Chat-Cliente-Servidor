import socket

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect(('localhost', 8888))



Duvida = False
print('Está com problemas em sua conexão? ')
Terminado = False
print('Digite finalizar para terminar o chat')

while not Terminado:
  cliente.send(input('Mensagem: ').encode('utf-8'))
  msg = cliente.recv(1024).decode('utf-8')
  if msg == 'finalizar':
    Terminado = True
  if msg == 'FINALIZAR':
    Terminado = True
  if msg == 'Finalizar':
    Terminado = True
  else:
    print(msg)
cliente.close()

while not Duvida:
  cliente.send(input('Mensagem: ').enconde('utf-8'))
  msg = cliente.recv(1024).decode('utf-8')
  if msg == 'sim':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
  if msg == 'SIM':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
  if msg == 'Sim':
    print('Aguarda Um momento que estaremos de transferindo para um representante legal ')
    
  if msg == 'Não':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()

if msg == 'nao':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()
if msg == 'NAO':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()
if msg == 'Nao':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()
if msg == 'Não':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()
if msg == 'NÃO':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()
if msg == 'não':
      print('Ok Estaremos encerrando o seu atendimento ')
      print(msg)
cliente.close()

      


    
    
    
