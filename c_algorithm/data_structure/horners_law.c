// https://dokhakdubini.tistory.com/185?category=847037
#include <stdio.h>
#define MAX_SIZE 101

double horner(int *coeff, int n, int x);

int main() {

	int coeff[MAX_SIZE] = { 1, 2, 3, 4, 5 };	// 1 + 2x + 3x^2 + 4x^3 + 5x^4
	int n=5;									//몇차다항식인지 알려주는 상수
	double result, x;

	printf("x의 값은? ");
	scanf(" %lf", &x);

	result = horner(coeff, n, x);

	printf("다항식 ");
	for (int i = n - 1; i >= 0; i--) {
		if (i == 0) {
			printf("%d", coeff[i]);
			break;
		}
		if (coeff[i] == 0)
			continue;

		printf("%d*x^%d + ", coeff[i], i);
	}
	printf("에서 x = %.1f일때 다항식의 값은 %.1f입니다.", x, result);

	return 0;
}

double horner(int *coeff, int n, int x) {
	//n번의 덧셈과 n번의 곱셈으로 해결
	double result = coeff[n - 2] + coeff[n-1] * x;

	for (int i = n - 3; i >= 0; i--) {
		result = result * x + coeff[i];
	}

	return result;
}
