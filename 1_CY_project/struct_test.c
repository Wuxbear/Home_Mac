
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

enum type {
    ET1 = 0x00,
    ET2 = 0x01,
    MT3 = 0x20,
};

struct tag {
    unsigned int len;
    char data[0];

};

struct et {
    enum type cmd;
    unsigned int len;
    char data[0];
};

int main(int argc, char **argv)
{
    char stt[] = "0123456789";
    int l = sizeof(stt);
    struct tag *p = (struct tag*) malloc(sizeof(struct tag) + l);
    p->len = l;
    memcpy(p->data, stt, l);
    printf("struct size %d\n", sizeof(struct tag));
    printf("%d, %s\n", p->len, p->data);
    free(p);
    return 0;
}

