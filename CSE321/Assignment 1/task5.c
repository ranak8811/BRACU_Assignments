#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
  pid_t c1, gc1, gc2, gc3;
  
  printf("1. Parent ID: %d\n", getpid());
  
  c1 = fork();
  
  if (c1 < 0){
    printf("Child 1 fork failed");
    return -1;
  }
  else if (c1 == 0){
    c1 = getpid();
    gc1 = fork();
    
    if (gc1 < 0){
      printf("Grand child 1 fork failed");
      return -1;
    }
    else if (gc1 > 0){
      gc2 = fork();
      
      if (gc2 < 0){
        printf("Grand child 2 fork failed");
        return -1;
      }
      else if (gc2 > 0){
        gc3 = fork();
        
        if (gc3 < 0){
          printf("Grand child 3 fork failed");
          return -1;
        }
        else if (gc3 > 0){
          printf("2. Child ID: %d\n", c1);
          printf("3. Grand child ID: %d\n", gc1);
          printf("4. Grand child ID: %d\n", gc2);
          printf("5. Grand child ID: %d\n", gc3);
        }
      }
    }
  }
}
