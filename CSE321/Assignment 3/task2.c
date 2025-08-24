#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>
#include <sys/ipc.h>
#include <sys/msg.h>

struct msg {
  long int type;
  char txt[6];
};

int main() {
  struct msg message;
  char buf[10];
  
  int msg_id = msgget(102, IPC_CREAT | 0666);
  
  printf("Please enter the workspace name:\n");
  
  int index = read(0, buf, sizeof(buf));
  buf[index] = '\0';
  
  if (strcmp(buf, "cse321\n") != 0) {
    printf("Invalid workspace name!\n");
    return -1;
  }
  
  strcpy(message.txt, buf);
  message.type = 1;
  
  msgsnd(msg_id, &message, sizeof(message.txt), 0);
  printf("Workspace name sent to otp generator from log in: %s\n", message.txt);
  
  pid_t pid = fork();
  
  if (pid < 0) {
    perror("Fork creation failed.\n");
    return -1;
  }
  else if (pid == 0) {
    msgrcv(msg_id, &message, sizeof(message.txt), 1, 0);
    printf("OTP generator received workspace name from log in: %s\n", message.txt);
    
    char otp[6];
    pid_t x = getpid();
    sprintf(otp, "%d", x);
    
    strcpy(message.txt, otp);
    message.type = 2;
    
    printf("OTP generator received workspace name from log in: %s\n", message.txt);
    msgsnd(msg_id, &message, sizeof(message.txt), 0);
    
    message.type = 3;
    
    msgsnd(msg_id, &message, sizeof(message.txt), 0);
    printf("OTP sent to mail from OTP generator: %s\n", message.txt);
    
    pid_t pid2 = fork();
    
    if (pid2 < 0) {
      perror("Fork creation failed.\n");
      return -1;
    }
    
    else if (pid2 == 0) {
      msgrcv(msg_id, &message, sizeof(message.txt), 3, 0);
      printf("Mail recieved OTP from OTP generator: %s\n", message.txt);
      
      message.type = 4;
      msgsnd(msg_id, &message, sizeof(message.txt), 0);
      printf("OTP sent to log in from mail: %s\n", message.txt);
      
      return 0;
    }
    
    else {
      wait(NULL);
    }
  }
  
  else {
    wait(NULL);
    char char1[6];
    char char2[6];
    
    msgrcv(msg_id, &message, sizeof(message.txt), 2, 0);
    
    strcpy(char1, message.txt);
    printf("Log in recieved OTP from OTP generator: %s\n", message.txt);
    
    msgrcv(msg_id, &message, sizeof(message.txt), 4, 0);
    
    strcpy(char2, message.txt);
    printf("Log in received OTP from mail: %s\n", message.txt);
    
    if (strcmp(char1, char2) == 0) {
      printf("OTP Verified!\n");
    }
    else {
      printf("OTP Incorrect!\n");
    }
    
    msgctl(msg_id, IPC_RMID, NULL);
 }
}
