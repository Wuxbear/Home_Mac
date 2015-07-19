
ifndef CROSS_COMPILE
	CC ?= gcc
else
	CC ?= gcc-cross-ooxx
endif

CFLAGS ?=
INC ?= -I include
LIB ?= -ldl

STATIC_LIB_FLAGS ?= -static
SHARED_LIB_FLAGS ?= -shared
DYNAMIC_LIB_FLAGS ?= -fPIC -shared

EIS_DAEMON_SRC = $(wildcard eis-daemon/*.c)
EIS_DAEMON_OBJ = $(patsubst %.c,%.o,$(wildcard eis-daemon/*.c))

EIS_LIBS_SRC = $(wildcard eis-libs/*.c)
EIS_LIBS_OBJ = $(patsubst %.c,%.o,$(wildcard eis-libs/*.c))

EIS_PLUGINS_SRC = $(wildcard eis-plugins/*.c)
EIS_PLUGINS_OBJ = $(patsubst %.c,%.o,$(wildcard eis-plugins/*.c))

.SUFFIXES:
.SUFFIXES: .c .o
.PHONY: clean install

all : eis_lib.so eis_plugin.so eis_daemon

eis_daemon: $(EIS_DAEMON_OBJ)
	@echo "build daemon"
	#$(CC) $(CFLAGS) -c $(EIS_DAEMON_OBJ)
	$(CC) $(CFLAGS) $(INC) $(LIB) -o $@ $(EIS_DAEMON_OBJ)

eis_lib.so: $(EIS_LIBS_OBJ)
	@echo "build eis_lib.so"
	$(CC) $(CFLAGS) $(DYNAMIC_LIB_FLAGS) -o $@ $<

eis_plugin.so: $(EIS_PLUGINS_OBJ)
	@echo "build eis_plugin.so"
	$(CC) $(CFLAGS) $(DYNAMIC_LIB_FLAGS) -o $@ $<

%.o : %.c
	$(CC) $(CFLAGS) -c $< -o $@

install:
	@echo "copy lib and daemon to rootfs folder."

clean:
	-rm -f eis-daemon/*.o eis-libs/*.o eis-plugins/*.o
	-rm -f eis_daemon eis_lib.so eis_plugin.so

