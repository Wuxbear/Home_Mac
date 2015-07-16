#ifndef __FILE_HEADER__
#define __FILE_HEADER__

void save_file(char *file, int len, char *dir);

int open_file(char *filename, unsigned int flag);
void close_file(int fd);
int file_append(int fd, char *data, int leng);
int write_file(int fd, char *data, int leng);

struct SRes {
	int nId;
	float fTemp;
	float fVolt;
	int nCurrent;
};

void save_log(struct SRes *res);
void save_temp_log(struct SRes *res);
int parser(char *resData, struct SRes *res);

#endif