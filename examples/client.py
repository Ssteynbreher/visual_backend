import socket

# Создаем сокет
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Подключаемся к серверу
client_socket.connect(('localhost', 12345))

# Отправляем данные серверу много раз
for i in range(10):  # Отправим 10 сообщений
    message = f'Hello, server!'.encode()
    client_socket.sendall(message)
    print(f"Отправлено: {message}")

# Закрываем соединение
client_socket.close()