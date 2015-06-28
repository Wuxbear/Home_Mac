
#include <stdio.h>
#include "include/uart_lib.h"
#include "include/net_lib.h"


int main(int argc, char ** argv)
{
        printf("yo!\n");

        /* psudo code flow
         * 1. get input argument, read config file
         * 2. support start, stop, restart
         * 3. run a daemon at background
         * 4. use socket to communation
         * 5. manager plugin, link list, thread or process ?
         * 6. control the MCU, command, data
         * 7. suport debug test command 
         */

        return 0;
}
