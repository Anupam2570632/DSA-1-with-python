#include <stdio.h>
int main()
{
    int arr[3][3] = {
        {3, 5, 2},
        {2, 6, 0},
        {3, 8, 9}};

    for (int i = 0; i < 3; i ++)
    {
        for (int j = 0; j < 3; j++)
        {
            printf("%x\n", &arr[i][j]);
        }
    }
}