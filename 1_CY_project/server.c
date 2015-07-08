#include <stdio.h>
#include <string.h>
#include <sys/socket.h>
#include <sys/wait.h>
#include <signal.h>
#include <arpa/inet.h>
#include <unistd.h>

#define DAEMON_IP  "127.0.0.1"
#define DAEMON_LISTEN_PORT  8888
#define DAEMON_BUFFER_SIZE  2048 

volatile sig_atomic_t daemon_going = 1;

void daemon_terminate_handler(int signum);

void daemon_terminate_handler(int signum)
{
    daemon_going = 0;
    signal(signum, daemon_terminate_handler)
    //stop thread or release resource before kill daemon
}

int main(int argc, char **argv)
{
    int socket_desc, client_sock, c, read_size;
    struct sockaddr_in server, client;
    char client_message[DAEMON_BUFFER_SIZE];
    
    if (signal(SIGTERM, daemon_terminate_handler) == SIG_IGN) {
        signal(SIGTERM, SIG_IGN);
    }
    signal(SIGINT, SIG_IGN);
    signal(SIGHUP, SIG_IGN);

    socket_desc = socket(AF_INET, SOCK_STREAM, 0);
    if (socket_desc == -1) {
        printf("could not create socket!");
        return 1;
    }
    
    server.sin_family = AF_INET;
    server.sin_addr.s_addr = inet_addr(DAEMON_IP);
    server.sin_port = htons(DAEMON_LISTEN_PORT);
    bzero(&(server.sin_zero),8);

    if(bind(socket_desc,(struct sockaddr *)&server, sizeof(server)) < 0) {
        perror("bind fail!");
        return 1;
    }

    if (listen(socket_desc, 5) == -1) {
        perror("listen fail!");
        return 1;
    }

    fflush(stdout);

    while (daemon_going) {
        c = sizeof(struct sockaddr_in);
        client_sock = accept(socket_desc, (struct sockaddr *)&client, (socklen_t *) &c);
        if (client_sock < 0) {
            perror("accept fail!");
            return 1;
        }
        
        while ((read_size = recv(client_sock, client_message, 2000, 0)) > 0) {
            write(client_sock, client_message, strlen(client_message));    
        }
    } 
   
    /*
    if (read_size == 0) {
        puts("disconnect!");
        fflush(stdout);
    }
    else if (read_size == -1)
    {
        perror("recv error!");
    }
    */
    close(socket_desc);
    return 0;
}

