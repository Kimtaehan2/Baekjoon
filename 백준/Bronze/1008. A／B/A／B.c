#include <stdio.h>
int main()
{
	int a, b;
	scanf("%d %d", &a, &b);
	printf("%.09f", (double)a / b);
	return 0;
}