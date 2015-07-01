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

    signal(SIGCHLD, SIG_IGN);
    signal(SIGHUP, SIG_IGN);


    pid = fork();

    if (pid < 0)
        exit(EXIT_FAILURE);

    if (pid > 0)
        exit(EXIT_SUCCESS);

    umask(0);

    chdir("/");

    int x;
    for (x = sysconf(_SC_OPEN_MAX); x > 0; x--)
    {
        close(x);
    }
}

void daemon_control(char *action)
{
    if ( 0 == strcmp(action,"start")) {
        printf("%s\n", action);
        //skeleton_daemon();
    }
    else if ( 0 == strcmp(action,"stop")) {
        printf("%s\n", action);
        /* kill daemon*/
        //system(kill -9 `pidof daemon`)
        exit(EXIT_SUCCESS);
    }
    else if ( 0 == strcmp(action,"restart")) {
        printf("%s\n", action);
        /* kill and restart daemon*/
    }
    else {
        printf("-a %s: Not support this action!\n", action);
        exit(EXIT_FAILURE);
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
    if (argc < 4) {
        printf("try \'%s -h\' for usage.\n", argv[0]);
    }

    while((ch = getopt(argc, argv, "a:c:s:h")) != -1)
    {
        switch(ch)
        {
            case 'a':
                daemon_control(optarg);
                break;
        }

    }
    
    optind = 1;
    while((ch = getopt(argc, argv, "a:c:s:h")) != -1)
    {
        switch(ch)
        {
            case 'a':
                break;
            case 'c':
                printf("c option!: %d, %s\n", optind, optarg);
                break;
            case 's':
                printf("s option!: %d, %s\n", optind, optarg);
                break;
            case 'h':
            default:
                usage();
        }

    }

    openlog ("daemon", LOG_PID, LOG_DAEMON);
    while(1)
    {
        syslog(LOG_NOTICE, "daemon started.");
        sleep(30);
        break; 
    }
    syslog(LOG_NOTICE, "daemon terminated.");
    closelog();
    return EXIT_SUCCESS;

}


