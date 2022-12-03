#include <stdio.h>
void fibonacci(int M)
{
	int one,result = 0;
	int two = 1;
	for (int i = 0; i <= M; i++)
	{
		one = two;
		two = result;
		result = one + two;
	}
	printf("%d %d\n", one, two);
}
int main()
{
	int N;
	scanf("%d", &N);
	int M;
	for (int i = 0; i < N; i++)
	{
		scanf("%d", &M);
		fibonacci(M);
	}
	return 0;
}
