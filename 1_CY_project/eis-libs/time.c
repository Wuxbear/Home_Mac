#include <time.h>
#include <stdio.h>
#include <stdlib.h>

char * time_number (void)
{
    char buf[512]={0};
    time_t t1 = time(NULL);
    struct tm *ptr = localtime(&t1);
    int year = ptr->tm_year + 1900;
    int month = ptr->tm_mon + 1;
    int hour = ptr->tm_hour;
    int min = ptr->tm_min;
    int sec = ptr->tm_sec;
    int day = ptr->tm_mday;

    sprintf(buf,"%d-%d-%d %d:%d:%d",year,month,day,hour,min,sec);

    return buf;
}
