#include <dlfcn.h>
#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv)
{
    void *handle;
    int (*fp)(void *dd);
    char *errmsg;

    handle = dlopen("libx.so", RTLD_LAZY);
    if (!handle) {
        fprintf(stderr, "%s\n", dlerror());
        exit(1);
    }

    dlerror();

    fp = dlsym(handle, "fp");
    if ((errmsg = dlerror()) != NULL) {
        fprintf(stderr, "%s\n", dlerror());
        exit(1);
    }

    (*fp)(errmsg);
    dlclose(handle);
    return 0;
}

