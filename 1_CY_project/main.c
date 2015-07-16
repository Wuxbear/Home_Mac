#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <syslog.h>
#include <dlfcn.h>
#include <signal.h>
#include <sys/socket.h>
#include <arpa/inet.h>

#include "include/uart_lib.h"
#include "include/net_lib.h"
#include "include/cmd.h"

#define DAEMON_NAME  "daemon"
#define DAEMON_IP  "127.0.0.1"
#define DAEMON_LISTEN_PORT  8888
#define DAEMON_BUFFER_SIZE  2048 

#define UART_LIB_NAME "uart_lib.so"

volatile sig_atomic_t daemon_going = 1;

enum DAEMON_ACTION {
    DAEMON_START = 0x0,
    DAEMON_STOP,
    DAEMON_RESTART,
};


/* Default plugins path 
 * /var/share/eis/plugins
 *
 * Customer plugins path
 * ~/eis/plugins
 *
 * configuration file path
 * /etc/eis/eis.conf
 */

/*
int load_dynamic_lib(void)
{
    void *lib_p;
    //int (*fp)(void *);
    fp_t fp;
    char *errmsg;

    lib_p = dlopen(UART_LIB_NAME, RTLD_NOW);
    if (!lib_p) {
        fprintf(stderr, "%s\n", dlerror());
        return 1;
    }
    //clear err msg buf
    dlerror();
    fp = dlsym(lib_p, "fp");
    if ((errmsg = dlerror()) != NULL) {
        fprintf(stderr, "%s\n", dlerror());
        return 1;
    }

    (*fp)(errmsg);
    dlclose(lib_p);
    return 0;
}
*/

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

void usage(void)
{ 
    printf("\n\
    usage: daemon -a action -c config_file -s MCU_cmd\n\
        -a <start/stop/restart>\n\
            start: start daemon\n\
            stop: stop daemon\n\
            restart: restart daemon\n\
        -c <config_file>\n\
        -s <read/write> <reg> <data>\n\
        -h display usage\n");

}

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


int main(int argc, char ** argv)
{
        /* psudo code flow
         * 1. get input argument, read config file
         * 2. support start, stop, restart
         * 3. run a daemon at background
         * 4. use socket to communation
         * 5. manager plugin, link list, thread or process ?
         * 6. control the MCU, command, data
         * 7. suport debug test command 
         */
    int ch;
    enum DAEMON_ACTION d_act;

    if (argc < 5) {
        usage();
        return 1;
    }

    while((ch = getopt(argc, argv, "a:c:s:h")) != -1)
    {
        switch(ch)
        {
            case 'a':
                if ( 0 == strcmp(optarg,"start")) {
                    d_act = DAEMON_START;
                }
                else if ( 0 == strcmp(optarg,"stop")) {
                    d_act = DAEMON_START;
                }
                else if ( 0 == strcmp(optarg,"restart")) {
                    d_act = DAEMON_START;
                }
                else {
                    printf("None support command!n");
                    return 1;
                }
                break;
            case 'c':
                printf("c option!: %d, %s\n", optind, optarg);
                // load the file name: config_file
                break;
            case 's':
                printf("s option!: %d, %s\n", optind, optarg);
                // ??
                break;
            case 'h':
            default:
                usage();
                return 1;
        }

    }

    // handle the daemon on/off
    daemon_control(d_act);

    // load config file

    // initial function pointer
    //load_dynamic_lib();

    // daemon loop
    openlog(DAEMON_NAME, LOG_PID, LOG_DAEMON);
    syslog(LOG_NOTICE, "daemon start.");

    if (daemon_loop()) {
        syslog(LOG_NOTICE, "daemon loop fail.");
        closelog();
        return EXIT_FAILURE;
    }
    else {
        syslog(LOG_NOTICE, "daemon terminated.");
        closelog();
        return EXIT_SUCCESS;
    }
}

