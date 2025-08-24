#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/shm.h>


struct shared {
  char sel[100];
  int b;
};

int main() {
  char select_val[100];
  
  int shm_id = shmget((key_t)101, 1024, IPC_CREAT | 0666);
  
  if (shm_id == -1) {
    perror("Shared memory creation failed\n");
    return -1;
  }
 
  struct shared *onl_bank = (struct shared *)shmat(shm_id, NULL, 0);
  
  int fd[2];
  int pipe1 = pipe(fd);
  
  if (pipe1 == -1) {
    perror("Pipe creation failed\n");
    return -1;
  }
  
  printf("Provide Your Input From Given Options:\n");
  printf("1. Type a to Add Money.\n");
  printf("2. Type w to Withdraw Money.\n");
  printf("3. Type c to Check Balance.\n\n");
  
  fgets(select_val, sizeof(select_val), stdin);
  
  strcpy(onl_bank -> sel, select_val);
  onl_bank -> b = 1000;
  
  printf("\nYour selection: %s\n", select_val);
  onl_bank -> sel[2] = '\0';
  
  pid_t pid = fork();

  if (pid == -1) {
    perror("Process creation failed\n");
    return -1;
  }
  else if (pid > 0) {
    wait(NULL);
    close(fd[1]);
    
    char buf[100];
    read(fd[0], buf, sizeof(buf));
    printf("%s", buf);
    
    close(fd[0]);
    shmctl(shm_id, IPC_RMID, NULL);
  }
  else {
    close(fd[0]);
    
    if (strcmp(onl_bank -> sel, "a\n") == 0) {
      int add_money;
      
      printf("Enter amount to be added:\n");
      scanf("%d", &add_money);
      
      if (add_money <= 0) {
        printf("Adding failed, Invalid amount.\n");
      }
      else {
        onl_bank -> b = onl_bank -> b + add_money;
        printf("Balanced added successfully!\n");
        printf("Updated balance after addition:\n");
        printf("%d\n", onl_bank -> b);
      }
    }
    
    else if (strcmp(onl_bank -> sel, "w\n") == 0) {
      int withdraw;
      
      printf("Enter amount to be withdrawn:\n");
      scanf("%d", &withdraw);
      
      if ((withdraw <= 0) || (withdraw > onl_bank -> b)) {
        printf("Withdrawal failed, Invalid amount\n");
      }
      else {
        onl_bank -> b = onl_bank -> b - withdraw;
        printf("Balance withdrawn successfully!\n");
        printf("Updated balance after withdrawal:\n");
        printf("%d\n", onl_bank -> b);
      }
    }
    
    else if (strcmp(onl_bank -> sel, "c\n") == 0) {
      printf("Your current balance is:\n");
      printf("%d\n", onl_bank -> b);
    }
    
    else {
      printf("Invalid Selection.\n");
    }
    
    char greetings[100] = "Thank you for using!\n";
    write(fd[1], greetings, strlen(greetings) + 1);
    close(fd[1]);
  }
}
