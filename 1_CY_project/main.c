#include <unistd.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <syslog.h>

#include "include/uart_lib.h"
#include "include/net_lib.h"

enum DAEMON_ACTION {
    DAEMON_START = 0x0,
    DAEMON_STOP,
    DAEMON_RESTART,
};

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

    //Signal handle
    signal(SIGCHLD, SIG_IGN);
    signal(SIGHUP, SIG_IGN);
    //Whe it get the kill signal, release resource and close thread ,process.


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
    if (argc < 4) {
        printf("try \'%s -h\' for usage.\n", argv[0]);
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
        }

    }

    // handle the daemon
    daemon_control(d_act);

    // load config file
    // call paser
    // daemon loop
    openlog ("daemon", LOG_PID, LOG_DAEMON);
    syslog(LOG_NOTICE, "daemon started.");
    while(1)
    {
        sleep(30);
        break; 
    }
    syslog(LOG_NOTICE, "daemon terminated.");
    closelog();
    return EXIT_SUCCESS;

}


