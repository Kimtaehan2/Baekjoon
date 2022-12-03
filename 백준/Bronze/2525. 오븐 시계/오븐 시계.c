#include <stdio.h>

int main(void)
{
    int H, M;
    scanf("%d %d", &H, &M);
    int T;
    scanf("%d", &T);
    if (M + T < 60)
        printf("%d %d", H, M + T);
    else if (H + ((M + T) / 60) >= 24)
        printf("%d %d", H + ((M + T) / 60) - 24, (M + T) % 60);
    else if (M + T >= 60)
        printf("%d %d", H + ((M + T) / 60), (M + T) % 60);
    
    return 0;
}