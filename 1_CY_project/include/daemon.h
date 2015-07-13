#ifndef __DAEMON_H__
#define __DAEMON_H__

enum DAEMON_ACTION {
    DAEMON_START = 0x0,
    DAEMON_STOP,
    DAEMON_RESTART,
};

static void skeleton_daemon();
void daemon_control(enum DAEMON_ACTION d_act);
void daemon_terminate_handler(int signum);
int daemon_loop(void);

#endif

