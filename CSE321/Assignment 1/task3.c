#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <string.h>

int main() {
  pid_t a, b, c, p1;
  p1 = getpid();
  char buffer[20];
  
  int file = open("./newfile.txt", O_CREAT | O_RDWR | O_TRUNC, 0666);
  printf("Wait!!! output is generating\n");
  
  a = fork();
  b = fork();
  c = fork();
  
  write(file, "+", 1);
  
  if (getpid() % 2 == 1){
    write(file, "+", 1);
    fork();
  }
  
  sleep(3);
  
  if (p1 == getpid()){
    lseek(file, 0, SEEK_SET);
    int byte_size = read(file, buffer, sizeof(buffer));
    buffer[byte_size] = '\0';
    printf("Porcess count: %zu\n", strlen(buffer));
  }
}
