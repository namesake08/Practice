#include<stdlib.h>

void bubble_sort(int *arr, int n)
{
    //can be implemented in more efficient way
    for (int i = 0; i < n; i++)
    {
        for(int k = 0; k < n - 1; k++)
	{
            if(arr[i] < arr[k])
            {
                //swap
		int tmp = arr[i];
		arr[i] = arr[k];
		arr[k] = tmp;
	    }
	}
    }
}

int main(void)
{
    int n = 20;
    int *arr = malloc(sizeof(int) * n);

    bubble_sort(arr, n);

    return 0;
}
