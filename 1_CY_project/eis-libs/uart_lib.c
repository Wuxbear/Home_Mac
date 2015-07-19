//#include "include/uart_lib.h"
#include <stdio.h>
#include <pthread.h>

//mutex protect
pthread_mutex_t uart_mutex;
//import uart port from config file

void uart_open()
{
    printf("uart_open!\n");
    //use the default attribute
    pthread_mutex_init(&uart_mutex, NULL);
}

void uart_close()
{
    printf("uart_close!\n");
    pthread_mutex_destroy(&uart_mutex);
}
void uart_write()
{
    printf("uart_write!\n");
    pthread_mutex_lock(&uart_mutex);
    // uart write data
    pthread_mutex_unlock(&uart_mutex);
}

void uart_read()
{
    printf("uart_read!\n");
    pthread_mutex_lock(&uart_mutex);
    //uart read data
    pthread_mutex_unlock(&uart_mutex);
}


