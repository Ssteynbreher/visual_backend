#include <winsock2.h>
#include <stdio.h>
#include <string.h>

#define PORT 12345
#define BUFFER_SIZE 1024

void run_client(const char *host, int port)
{
    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == INVALID_SOCKET)
    {
        printf("Ошибка создания сокета\n");
        return;
    }

    struct sockaddr_in serv_addr;
    memset(&serv_addr, 0, sizeof(serv_addr));
    serv_addr.sin_family = AF_INET;
    serv_addr.sin_port = htons(port);
    serv_addr.sin_addr.s_addr = inet_addr(host);

    if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) == SOCKET_ERROR)
    {
        printf("Ошибка подключения\n");
        closesocket(sock);
        return;
    }

    printf("Подключение к серверу %s:%d\n", host, port);

    char *message = "Hello World!";
    send(sock, message, strlen(message), 0);
    printf("Отправлено серверу: %s\n", message);

    char buffer[BUFFER_SIZE];
    int valread = recv(sock, buffer, BUFFER_SIZE - 1, 0);
    if (valread > 0)
    {
        buffer[valread] = '\0';
        printf("Получено от сервера: %s\n", buffer);
    }
    else if (valread == 0)
    {
        printf("Соединение закрыто сервером\n");
    }
    else
    {
        printf("Ошибка приема данных\n");
    }

    closesocket(sock);
}

int main(int argc, char *argv[])
{
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) != 0)
    {
        printf("Ошибка инициализации Winsock\n");
        return 1;
    }

    int port = (argc > 1) ? atoi(argv[1]) : PORT;
    run_client("127.0.0.1", port);

    WSACleanup();
    getchar();

    return 0;
}