//https://dokhakdubini.tistory.com/191?category=847037
#include <stdio.h>

int factorial(int n);

int main() {
	int n;

	printf("n의 값을 입력하세요: ");
	scanf(" %d", &n);

	printf("n! = %d", factorial(n));

}

int factorial(int n) {
	if (n <= 1)
		return 1;
	else
		return n * factorial(n - 1);
}
