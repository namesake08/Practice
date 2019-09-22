#include <stdio.h>
#include <stdlib.h>
#define	arraySize 5

int main(){
    int sum = 0;
    int arr[] = {1,3,8,10,2};
    for(int i = 0; i < arraySize; ++i){
        sum += arr[i];
    }
    printf("The sum is : %d\n",sum);
}
