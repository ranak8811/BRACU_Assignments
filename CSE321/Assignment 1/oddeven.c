#include <stdio.h>
#include <stdlib.h>

int main(int argc, char *argv[]){
  int count = argc -1;
  int arr[count];
  
  for (int i = 1; i < argc; i++){
    arr[i-1] = atoi(argv[i]);
  }
  
  for (int j = 0; j < count; j++){
    if (arr[j] % 2 == 0){
      printf("Even number: %d\n", arr[j]);
    }
    else {
      printf("Odd number: %d\n", arr[j]);
    }
  }
}
