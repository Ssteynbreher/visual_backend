# server.py
import zmq
import time

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

print("ZMQ сервер запущен на порту 5555...")

received_count = 0
log_file = open("android_messages.log", "a", encoding="utf-8")

try:
    while True:
        message = socket.recv()
        received_count += 1
        msg_str = message.decode('utf-8')

        print(f"[{received_count}] Получено от Android: {msg_str}")
        log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} | {msg_str}\n")
        log_file.flush()

        time.sleep(1)
        reply = "Hello from Server!"
        socket.send(reply.encode('utf-8'))
        print(f"    Отправлен ответ: {reply}")

except KeyboardInterrupt:
    print("\nСервер остановлен")
finally:
    log_file.close()
    socket.close()
    context.term()