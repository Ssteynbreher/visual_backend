import socket
import sys


def run_server(host='127.0.0.1', port=12345):
    """Запуск TCP сервера"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"Сервер запущен на {host}:{port}")
        print("Ожидание подключения...")

        conn, addr = server_socket.accept()
        with conn:
            print(f"Подключен клиент: {addr}")

            data = conn.recv(1024)
            if data:
                message = data.decode('utf-8')
                print(f"Получено от клиента: {message}")

                # Отправляем ответ
                response = f"Hello from Python Server! Your message: {message}"
                conn.sendall(response.encode('utf-8'))
                print(f"Отправлено клиенту: {response}")

if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 12345
    run_server(port=port)