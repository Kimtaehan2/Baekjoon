#include <stdio.h>
int main()
{
	static int sum = 0;
	char arr[101];
	int n;
	scanf("%d", &n);
	scanf("%s", arr, 101);
	for (int i = 0; i < n; i++)
	{
		int m = arr[i]-48;
		sum += m;
	}
	printf("%d", sum);
	return 0;
}