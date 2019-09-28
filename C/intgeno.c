#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void generate_data(int *arr, int n)
{
  srand(time(0));
  for (int i=0; i<n; i++)
  {
    arr[i] = rand() % 100 + 1;
  }
}

void print_data(int *arr, int n)
{
  printf("\n\nPrinting data...\n");

  for (int i=0; i<n; i++)
  {
    printf("\tCell %d: %d\n", i, arr[i]);
  }
}

int main(void)
{
    int n = 10;
    int *arr = malloc(sizeof(*arr) * n); 

    generate_data(arr, n);
    print_data(arr, n);
}
