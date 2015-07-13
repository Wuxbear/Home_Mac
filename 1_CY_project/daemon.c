
#include <string.h>
#include <sys/stat.h>
#include <signal.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include "include/daemon.h"

static void skeleton_daemon()
{
    pid_t pid;

    /* Fork off the parent process */
    pid = fork();

    /* An error occurred */
    if (pid < 0) {
        exit(EXIT_FAILURE);
    }
    else if (pid > 0) {
        exit(EXIT_SUCCESS);
    }
    /* On success: The child process becomes session leader */
    if (setsid() < 0)
        exit(EXIT_FAILURE);

    pid = fork();

    if (pid < 0) {
        exit(EXIT_FAILURE);
    }
    else if (pid > 0) {
        exit(EXIT_SUCCESS);
    }

    umask(0);

    chdir("/");

    int x;
    for (x = sysconf(_SC_OPEN_MAX); x > 0; x--)
    {
        close(x);
    }
}

void daemon_control(enum DAEMON_ACTION d_act)
{
    switch (d_act) {
        case DAEMON_START:
            skeleton_daemon();
            break;
        case DAEMON_STOP:
            // kill -9 `pidof daemon`
            break;
        case DAEMON_RESTART:
            // kill -9 `pidof daemon`
            skeleton_daemon();
            break;
    }
}

void daemon_terminate_handler(int signum)
{
    daemon_going = 0;
    printf("kill daemon!\n");
    //signal(signum, daemon_terminate_handler);
    //stop thread or release resource before kill daemon
}

int daemon_loop(void)
{
    int server_socket, client_socket, c, read_size;
    struct sockaddr_in server_sockaddr, client_sockaddr;
    char client_message[DAEMON_BUFFER_SIZE];
    
    if (signal(SIGKILL, daemon_terminate_handler) == SIG_IGN) {
        signal(SIGKILL, SIG_IGN);
    }
    signal(SIGINT, SIG_IGN);
    signal(SIGHUP, SIG_IGN);

    server_socket = socket(AF_INET, SOCK_STREAM, 0);
    if (server_socket == -1) {
        printf("could not create socket!");
        return 1;
    }
    
    bzero(&server_sockaddr, sizeof(server_sockaddr));
    server_sockaddr.sin_family = AF_INET;
    server_sockaddr.sin_addr.s_addr = inet_addr(DAEMON_IP);
    server_sockaddr.sin_port = htons(DAEMON_LISTEN_PORT);

    if(bind(server_socket,(struct sockaddr *)&server_sockaddr, sizeof(server_sockaddr)) < 0) {
        perror("bind fail!");
        return 1;
    }

    if (listen(server_socket, 5) == -1) {
        perror("listen fail!");
        return 1;
    }

    while (daemon_going) {
        c = sizeof(struct sockaddr_in);
        client_socket = accept(server_socket, (struct sockaddr *)&client_sockaddr, (socklen_t *) &c);
        if (client_socket < 0) {
            perror("accept fail!");
            return 1;
        }
        
        //command parser, switch case
        
        while ((read_size = recv(client_socket, client_message, 2000, 0)) > 0) {
            write(client_socket, client_message, strlen(client_message));    
        }
    } 
 
    close(server_socket);
    return 0;
}

