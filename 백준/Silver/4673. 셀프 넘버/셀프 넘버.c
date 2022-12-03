#include <stdio.h>
int d(int n) {
	int sum = n;
	while (n > 0)
	{
		sum += n % 10;
		n /= 10;
	}
	return sum;
}
int main()
{
	int self_num[10001];
	for (int i = 1; i < 10001; i++) {
		int check = d(i);
		if (check<10001)
			self_num[check] = 1;
	}
	for (int i = 1; i < 10001; i++) {
		if (self_num[i] != 1)
			printf("%d\n", i);
	}
	return 0;
}