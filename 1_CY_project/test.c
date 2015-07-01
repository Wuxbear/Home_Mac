#include <stdio.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <syslog.h>

static void skeleton_daemon()
{
    pid_t pid;

    /* Fork off the parent process */
    pid = fork();

    /* An error occurred */
    if (pid < 0)
        exit(EXIT_FAILURE);

    /* Success: Let the parent terminate */
    if (pid > 0)
        exit(EXIT_SUCCESS);

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


int main()
{
    skeleton_daemon();
    /* log on system (Ubuntu), /var/log/syslog */
    openlog ("firstdaemon", LOG_PID, LOG_DAEMON);
    while(1)
    {
        syslog(LOG_NOTICE, "First daemon started.");
        sleep(100);
        break; 
    }
    syslog(LOG_NOTICE, "First daemon terminated.");
    closelog();
    return EXIT_SUCCESS;
}


