#include <stdio.h>
#include <stdlib.h>

void showArrValues(int *arrP, int length){
  int i;
  for (i = 0; i < length; i++){
    printf("%d - ", arrP[i]);
  }
}

int main(int argc, char *argv[]){
  int count = argc -1;
  int arr[count];
  
  for (int i = 1; i < argc; i++){
    arr[i-1] = atoi(argv[i]);
  }
  
  for (int j = 0; j < count -1; j++){
    for (int k = 0; k < count - 1; k++){
      if (arr[k] < arr[k+1]){
        int swap = arr[k];
        arr[k] = arr[k+1];
        arr[k+1] = swap;
      }
    }
  }
  
  showArrValues(arr, count);
  printf("\n");
}
