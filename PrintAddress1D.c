#include <stdio.h>
int main()
{
    int arr[] = {3, 5, 2, 5, 6};

    for (int i = 0; i < sizeof(arr) / sizeof(arr[0]); i++)
    {
        printf("%d\n", &arr[i]);
    }
}