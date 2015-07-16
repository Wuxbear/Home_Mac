#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <errno.h>
#include <termios.h>
#include <sys/time.h>

#include "file.h"
#include "uart.h"
#include "configure.h"
#include "debug.h"

#define MAXNO(__A__, __B__) ((__A__ > __B__) ? __A__ : __B__)

int main( int argc, char **argv )
{
	char *path = NULL;
	char *mode = NULL;	
	int con = -1;
	struct termios info;
	char *command = NULL;
	char *device = NULL;
	char *ID = NULL;
	char *szLogFile[256]={0};
	char *szTempLog[256]={0};
	
	char buf[1024] = {0};
	int x = 0, maxfd = 0 , y = 0;
	int len = 0;
	int udp_server = -1;
	int timer = 0;
	char *group = NULL;
	fd_set fds;
	FILE *fp = NULL;
	char * delim = "/";
	char * pch;

	if (1 >= argc) {
		_DEBUG_MSG("not have arguments");
		return -1;
	}

	configure_init( argv[1] );

	device = get_conf("device");
	command = get_conf("command");
	path = get_conf("path");
	ID = get_conf("ID");
	mode = get_conf("mode");

	con = open_console(device);
	
	if (0 >= con) {
		_DEBUG_MSG("open serial port: %s failed", device);
		return -2;
	}
	
	tcgetattr(con, &info);
	con_setting(con);
	
	struct timeval tv = { .tv_sec=3, .tv_usec=0 };

	FD_ZERO(&fds);
	maxfd = 0;
	FD_SET(con, &fds);
	maxfd = MAXNO(con, maxfd);
	_DEBUG_MSG("set timeout");
	select(con+1, &fds, NULL, NULL, &tv); 
	
	while(1) {
		//if(FD_ISSET(con, &fds)) {
		memset(buf,0,sizeof(buf));
		
		//if(strcmp(mode,"server")  ) {
		write(con,command,strlen(command));
		//}			
		
		sleep(1);
		
		len = read(con, buf, sizeof(buf)-1);
		struct SRes res;
		
		//_DEBUG_MSG("read len: %d, data: %s", len, buf);     
		
		if(0 == parser(buf, &res)) {
			save_log(&res);
			save_temp_log(&res);
		}
		sleep(1);

		//}
	}

	con_close(con,&info);
	return 0;
}
