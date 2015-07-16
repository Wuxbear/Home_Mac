CFLAG=-DDEBUG

all: UART

main.o: main.c
	$(CC) $(CFLAG) -c -o $@ $^

configure.o: configure.c
	$(CC) -c $(CFLAG) -o $@ $^

command.o: command.c
	$(CC) -c $(CFLAG) -o $@ $^

uart.o: uart.c
	$(CC) -c $(CFLAG) -o $@ $^

file.o: file.c
	$(CC) -c $(CFLAG) -o $@ $^

time.o: time.c
	$(CC) -c $(CFLAG) -o $@ $^

UART: main.o configure.o commander.o uart.o file.o time.o
	$(CC) $(CFLAG) -o $@ $^ $(LDFLAGS)

clean:
	rm -f *.o con_test UART $(all)
