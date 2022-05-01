#include <stdio.h>

int combination(int n, int k);

int main() {
	int n, k;
	printf("차례대로 n과 k를 입력해주세요: ");
	scanf(" %d %d", &n, &k);

	printf("%dC%d = %d",n, k, combination(n, k));

	return 0;
}

int combination(int n, int k) {
	if (k == 0 || k == n)
		return 1;
	else
		return combination(n - 1, k - 1) + combination(n - 1, k);
}
