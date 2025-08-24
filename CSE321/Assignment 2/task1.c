#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <pthread.h>

int x = 0, y = 1;
int all_searches, all_numbers;

void *print_fibonacci_series(void *numbers);
void *show_fibonacci_results(void *numbers);

int main(void) {
  pthread_t t1, t2;
  
  do {
    printf("Enter the term of fibonacci sequence:\n");
    scanf("%d", &all_numbers);
  }
  while (all_numbers < 0 || all_numbers > 40);
  
  do {
    printf("How many numbers you are willing to search?:\n");
    scanf("%d", &all_searches);
  }
  while (all_searches < 0);
  
  all_searches = all_searches + 1;
  all_numbers = all_numbers + 1;
  
  int *nums = malloc(all_numbers * sizeof(int));
  
  pthread_create(&t1, NULL, print_fibonacci_series, (void *)nums);
  pthread_join(t1, NULL);
  
  pthread_create(&t2, NULL, show_fibonacci_results, (void *)nums);
  pthread_join(t2, NULL);
  
  free(nums);
}

void *print_fibonacci_series(void *numbers) {
  int *arr = (int *)numbers;
  
  arr[0] = x;
  arr[1] = y;
  
  printf("a[0] = %d\n", arr[0]);
  printf("a[1] = %d\n", arr[1]);
  
  for (int i = 2; i < all_numbers; i++) {
    arr[i] = arr[i-1] + arr[i-2];
    printf("a[%d] = %d\n", i, arr[i]);
  }
}

void *show_fibonacci_results(void *numbers) {
  int *arr = (int *)numbers;
  
  int index_value;
  
  for (int i = 1; i < all_searches; i++) {
    printf("Enter search %d\n", i);
    scanf("%d", &index_value);
    
    printf("result of search #%d = ", i);
    
    if ((index_value >= all_numbers) || (index_value < 0)) {
      printf("-1\n");
    }
    else {
      printf("%d\n", arr[index_value]);
    }
  }
}
