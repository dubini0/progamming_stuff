// https://dokhakdubini.tistory.com/192?category=847037
#include <stdio.h>

int fibonacci(int n);

int main() {
	int n;
	/*printf("이 프로그램은 피보나치 수열의 값을 계산하는 함수입니다.\n");
	printf("몇 번째 수열을 알고싶으신가요?: ");
	scanf(" %d", &n);*/

	for (int n = 0; n < 11; n++) {
		printf("f(%d) = %d\n", n, fibonacci(n));
	}
	return 0;
}

int fibonacci(int n) {
	if (n == 1)
		return 1;
	else if (n == 0)
		return 0;
	else
		return fibonacci(n - 1) + fibonacci(n - 2);
}
