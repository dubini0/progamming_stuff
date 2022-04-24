#include <stdio.h>	

int main() {
	int n=6, sum;

	printf("이 프로그램은 1부터 1000까지의 값들 중 제수와 자기자신이 같은지 확인하는 프로그램입니다.\n");
	for (n = 1; n <= 1000; n++) {
		sum = 0;
		for (int i = 1; i <= n / 2; i++) {
			if (n % i == 0) {
				sum += i;
			}

		}
		if (sum == n)
			printf("%d의 제수의 합은 자기자신과 같습니다.\n", n);
	}

	return 0;
}
