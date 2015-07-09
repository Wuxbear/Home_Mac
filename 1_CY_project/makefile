
CC ?= gcc
CFLAGS ?= -Wall
INC ?= -I include
LIB ?= -rdynamic -ldl
DYNAMIC_LIB_FLAGS ?= -fPIC -s shared

# static lib, -static
# share lib, -shared
# dynamic lib, -fPIC -shared

DAEMON_SRC = main.c
DAEMON_OBJ = $(DAEMON_SRC:%.c=%.o)
UART_LIB_SRC = uart_lib.c
UART_LIB_OBJ = $(UART_LIB_SRC:%.c=%.o)
NET_LIB_SRC = net_lib.c
NET_LIB_OBJ=  $(NET_LIB_SRC:%.c=%.o)

.SUFFIXES:
.SUFFIXES: .c .o
.PHONY: clean

all: daemon

test: test.c
	gcc -o test test.c

daemon: $(DAEMON_OBJ)
	@echo "build daemon"
	$(CC) $(CFLAGS) $(INC) $(LIB) -o $@ $(DAEMON_OBJ)

uart_lib.so:
	@echo "build uart_lib"
	# $(CC) $(CFLAGS) $(DYNAMIC_LIBS_FLAG) -o $@ $(DAEMON_OBJ)

net_lib.so:
	@echo "build net_lib"

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	-rm -f daemon *.o
