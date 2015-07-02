#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <arpa/inet.h>


int main(int argc, char ** argv)
{
    int sock;
    struct sockaddr_in server;
    char message[1000], server_reply[2000];
    sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == -1) {
        puts("socket create fail!");
    }
    
    server.sin_addr.s_addr = inet_addr("127.0.0.1");
    server.sin_family = AF_INET;
    server.sin_port = htons(8888);

    if (connect(sock, (struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("connect fail!");
        return 1;
    }

    while(1) {
        printf("enter message: ");
        scanf("%s", message);
        if (send(sock, message, strlen(message), 0) < 0) {
            puts("send fail!");
            return 1;
        }
        
        if (recv(sock, server_reply, 2000, 0) < 0) {
            puts("recv fail!");
            break;
        }
        printf("server reply: %s\n", server_reply);
    }

    close(sock);
    return 0;
}

