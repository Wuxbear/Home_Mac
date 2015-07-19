#include <dirent.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/statvfs.h>
#include <sys/stat.h>
#include <sys/types.h>
#include <fcntl.h>

#include "file.h"
#include "../include/debug.h"

#define LOG_FILE "log.txt"
#define LOG_PATH "/var/log"
#define TEMP_LOG_VOLT "vv.log"
#define TEMP_LOG_CURR "ii.log"
#define TEMP_LOG_TEMP "oo.log"
#define TEMP_LOG_OK "OK"
#define PAGE_FILE "/usr/share/eis/page"

int open_file(char *filename, unsigned int flag) {
		if (NULL == filename) {
			_DEBUG_MSG("the file name is null");
			return -1;
		}
		
		int nFd=open(filename, flag, 0666);
		return nFd;
}

void close_file(int fd) {
	if (0 >= fd)
		return;
	
	close(fd);
}

int file_append(int fd, char *data, int leng) {
	if (0 >= fd)
		return 0;
	
	lseek(fd, 0, SEEK_END);
	return write_file(fd, data, leng);	
}

int write_file(int fd, char *data, int leng) {
	if (0 >= fd)
		return 0;
		
	return (int) write(fd, data, leng);
}

void save_log(struct SRes *res) {
	if (NULL == res) return;
	
	char szPath[256]={0};
	
	sprintf(szPath, "%s/%d", LOG_PATH, res->nId);
	int nFD=open_file(szPath, O_DIRECTORY);
	
	if (0 >= nFD) {
		_DEBUG_MSG("log folder dose not exist, create it");
		mkdir(szPath, 0777);
	}
	
	//_DEBUG_MSG("the folder is exist store log");
	close_file(nFD);
	
	// log file
	sprintf(szPath, "%s/%d/%s", LOG_PATH, res->nId, LOG_FILE);
	nFD=open_file(szPath, O_CREAT | O_RDWR | O_APPEND | O_SYNC);
	
	if (0 >= nFD) {
		_DEBUG_MSG("create log.txt file failed");
		return;
	}
	
	char szData[100]={0};
	sprintf(szData, "%s|%0.1f|%0.2f|%d|\n", time_number(), res->fTemp, res->fVolt, res->nCurrent);
	file_append(nFD, szData, strlen(szData));
	close_file(nFD);
	
	nFD=open_file(PAGE_FILE, O_CREAT | O_RDWR | O_TRUNC | O_SYNC);
	if (0 >= nFD) {
		_DEBUG_MSG("create page file failed");
		return;
	}
	
	sprintf(szData, "%d", res->nId);
	write_file(nFD, szData, 1);	
	close_file(nFD);
	
}

void save_temp_log(struct SRes *res) {
	if (NULL == res) return;
	char szFile[256]={0};
	char szData[20];
	
	// temp
	sprintf(szFile, "%s/%d/%s", LOG_PATH, res->nId, TEMP_LOG_TEMP);
	int nFD=open_file(szFile, O_CREAT | O_RDWR | O_TRUNC | O_SYNC);
	
	sprintf(szData, "%0.1f", res->fTemp);
	write_file(nFD, szData, strlen(szData));
	
	close_file(nFD);
	
	// volt
	sprintf(szFile, "%s/%d/%s", LOG_PATH, res->nId, TEMP_LOG_VOLT);
	nFD=open_file(szFile, O_CREAT | O_RDWR | O_TRUNC | O_SYNC);
	
	sprintf(szData, "%0.2f", res->fVolt);
	write_file(nFD, szData, strlen(szData));	
	
	close_file(nFD);	
	
	// current
	sprintf(szFile, "%s/%d/%s", LOG_PATH, res->nId, TEMP_LOG_CURR);
	nFD=open_file(szFile, O_CREAT | O_RDWR | O_TRUNC | O_SYNC);

	sprintf(szData, "%d", res->nCurrent);
	write_file(nFD, szData, strlen(szData));	
	
	close_file(nFD);	
	
	// ok
	sprintf(szFile, "%s/%d/%s", LOG_PATH, res->nId, TEMP_LOG_OK);
	nFD=open_file(szFile, O_CREAT | O_RDWR | O_TRUNC | O_SYNC);

	write_file(nFD, "1", 1);	
	close_file(nFD);
}

int parser(char *resData, struct SRes *res) {
	if (NULL == resData || NULL == res) {
		_DEBUG_MSG("the parameter is null pointer");
		return -1;
	}
	if (0 == strlen(resData)) {
		_DEBUG_MSG("information string is null");
		return -2;
	}
	memset (res, 0, sizeof(struct SRes));
	// the format: ***2**   415 t/5132v/656 i########$
	int nTemp, nVolt, nCurrent;
	
	sscanf (resData, "***%d**   %d t/%dv/%d/i########$", &res->nId, &nTemp, &nVolt, &nCurrent);
	
	res->fTemp = (float) nTemp / 10.0;
	res->fVolt = (float) nVolt / 1000.0;
	res->nCurrent = nCurrent;
	
	if (0 == res->nId || 0 == res->fTemp || 0 == res->fVolt || 0 == res->nCurrent) {
		_DEBUG_MSG("data error");
		return -3;
	}
	//_DEBUG_MSG("id: %d, temp: %f, v: %f, c: %d", res->nId, res->fTemp, res->fVolt, res->nCurrent);

	return 0;
}

void save_file(char *file, int len, char *dir)
{
    char file_path[1024]={0};
    char buff_1[1024]={0};
    char buff_2[1024]={0};
    FILE *fp = NULL;
    int garbage,file_num;
    char path[1024] = {0};
    char id[4]={0};
    char dd[1]={0};
    char oo[2]={0};
    char oo_1[2]={0};
    char ii[4]={0};
    char vv[2]={0};
    char vv_1[1]={0};

	_DEBUG_MSG("mcu data: %s", file);

    if (len <= 0 )
        return;

    file += 3;
    strncpy(dd,file,1);
if(!strcmp(dd,"1"))
{
    system("rm -rf /var/log/1/OK");
    system("rm -rf /var/log/2/OK");
    system("rm -rf /var/log/3/OK");
    system("rm -rf /var/log/4/OK");
    system("rm -rf /var/log/5/OK");
    system("rm -rf /var/log/6/OK");
}
    
    sprintf(id,"00%s",dd);
    file += 6;
    strncpy(oo,file,2);
    file += 2;
    strncpy(oo_1,file,1);
    sprintf(buff_2,"/var/log/%s",dd);
    mkdir(buff_2,0777);
    sprintf(buff_1,"echo %s.%s > /var/log/%s/oo.log",oo,oo_1,dd);
    system(buff_1);
    file += 4;
    strncpy(vv,file,1);
    file += 1;
    strncpy(vv_1,file,2);
    sprintf(buff_1,"echo %s.%s > /var/log/%s/vv.log",vv,vv_1,dd);
    system(buff_1);
    file += 5;
    strncpy(ii,file,3);
    sprintf(buff_1,"echo %s > /var/log/%s/ii.log",ii,dd);
    system(buff_1);


    sprintf(buff_1,"echo 1 > /var/log/%s/OK",dd);
    system(buff_1);
    sprintf(file_path,"/var/log/%s/log.txt",dd);

    fp = fopen(file_path,"a"); 

    if(!fp){
	    return;
    }
    fprintf(fp,"%s|%s.%s|%s.%s|%s|\n",time_number(),oo,oo_1,vv,vv_1,ii);
    fclose(fp);
}

