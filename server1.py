from socket import *

Host = "localhost"
Port = 9090 #устанавливаем порт
addr = (Host, Port) #кортеж для хранения адреса сервера
sock = socket(AF_INET, SOCK_DGRAM) #создаем новый объект
sock.bind(addr) #привязываем к адресу
connections = []
print("Связь с клиентом установлена")
while True:
    conn, addr = sock.recvfrom(1024) #получение данных из сокета
    line = conn.decode() #декодируем строку
    print(conn.decode())
    line2 = input("Ответ клиенту: ")
    line2 = line2.encode()#приводим строку к байтам
    sock.sendto(line2, addr)#отправление данных в сокет
print("Соединение с клиентом прекращено")
conn.close()