
ifndef CROSS_COMPILE
	CC ?= gcc
else
	CC ?= gcc-cross-ooxx
endif

CFLAGS ?= -Wall
INC ?= -I include
LIB ?= -ldl

STATIC_LIB_FLAGS ?= -static
DYNAMIC_LIB_FLAGS ?= -fPIC -shared

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

uart_lib.so: $(UART_LIB_OBJ)
	@echo "build uart_lib.so"
	$(CC) $(CFLAGS) $(DYNAMIC_LIB_FLAGS) -o $@ $(UART_LIB_OBJ)

net_lib.so: $(NET_LIB_OBJ)
	@echo "build net_lib.so"
	$(CC) $(CFLAGS) $(DYNAMIC_LIB_FLAGS) -o $@ $(NET_LIB_OBJ)

%.o: %.c
	$(CC) $(CFLAGS) -c $<

clean:
	-rm -f daemon uart_lib.so *.o

