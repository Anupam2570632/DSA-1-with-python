#include <stdio.h>
#include <limits.h>
int main()
{
    int t;
    scanf("%d", &t);
    while (t--)
    {
        long long n;
        scanf("%lld", &n);

        long long a[n];
        for (long long i = 1; i <= n; i++)
        {
            scanf("%lld", &a[i]);
        }

        long long valueRight = n;
        long long valueLeft = n;


        for (long long i = 2; i <= n; i++)
        {

            if ((valueRight + 1 - i) == a[i])
            {
                valueRight = valueRight + (i - 1);
            }
        }
        
               for (long long i = n; i > 1; i--) {
            if ((valueLeft + 1 - i) == a[i]) {
                valueLeft = valueLeft + (i - 1);
            }
        }

        printf("%lld\n", (valueLeft > valueRight) ? valueLeft : valueRight);

    }
    return 0;
}