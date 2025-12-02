import socket
import sys


def run_client(host='127.0.0.1', port=12345):
    """Запуск TCP клиента"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        try:
            client_socket.connect((host, port))
            print(f"Подключение к серверу {host}:{port}")

            message = "Hello World!"
            client_socket.sendall(message.encode('utf-8'))
            print(f"Отправлено серверу: {message}")

            data = client_socket.recv(1024)
            response = data.decode('utf-8')
            print(f"Получено от сервера: {response}")

        except ConnectionRefusedError:
            print(f"Не удалось подключиться к {host}:{port}")
            print("   Убедитесь, что сервер запущен")


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 12345
    run_client(port=port)