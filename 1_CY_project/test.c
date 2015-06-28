#include <stdio.h>
#include <unistd.h>

void usage(void)
{ 
    printf("\
adfk\
adfkj\
adfk");

}
 

int main(int argc, char **argv)
{
    int ch;
    opterr = 0;
    while((ch = getopt(argc, argv, "a:bc")) != -1)
    {
        switch(ch)
        {
            case 'a':
                printf("a option!: %s\n", optarg);
                break;
            case 'b':
                printf("b option!\n");
                break;
            case 'c':
                printf("c option!\n");
                break;
            default:
                usage();
        }

    }

    return 0;
}
