//https://dokhakdubini.tistory.com/193?category=847037
#include <stdio.h>

int factorial(int n);
int combination(int n, int k);

int main() {
	int n, k;
	printf("차례대로 n과 k를 입력해주세요: ");
	scanf(" %d %d", &n, &k);

	printf("%dC%d = %d",n, k, combination(n, k));

	return 0;
}

int factorial(int n) {
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
}

int combination(int n, int k) {
	if (k<0 || k >n)
		return 0;
	else
		return factorial(n) / (factorial(k)*factorial(n - k));
}
