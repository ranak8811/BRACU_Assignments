#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main() {
  pid_t p1, p2;
  
  p1 = fork();
  
  if (p1 < 0) {
    printf("Parent fork failed");
  }
  else if (p1 == 0) {
    p2 = fork();
    
    if (p2 < 0){
      printf("Child fork failed");
    }
    else if (p2 == 0) {
      printf("I am grandchild\n");
    }
    else {
      wait(NULL);
      printf("I am child\n");
    }
  }
  else {
    wait(NULL);
    printf("I am parent\n");
  }
}
