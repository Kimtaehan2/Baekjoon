#include <stdio.h>
int main(void)
{	
	int year;
	scanf("%d", &year);
	int Year_S = ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0);
	printf("%d",Year_S);
	return 0;
}