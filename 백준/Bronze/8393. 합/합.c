#include <stdio.h>

int main(void)
{
    int static sum = 0;
    int n;
    scanf("%d", &n);
    for (int i = 1; i <= n; i++)
    {
        sum = sum + i;
    }
    printf("%d", sum);
    return 0;
}