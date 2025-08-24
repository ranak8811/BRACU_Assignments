#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char *argv[]){
  pid_t p1;
  
  p1 = fork();
  
  if (p1 < 0){
    printf("Fork failed");
    return -1;
  }
  else if (p1 == 0){
    execv("./sort", argv);
  }
  else {
    wait(NULL);
    execv("./oddeven", argv);
  }
}
