#include <stdio.h>
int main(void){
	int n;
	scanf("%d", &n);
	for (int i = 1; i <= n; i++) {
		for (int j = n-1; j >= i; j--) {
			printf(" ");
		}
		for (int k = 1; k <= i; k++) {
			printf("*");
		}
		printf("\n");
	}
	return 0;
}