#include <stdio.h>

int ackermann(int m, int n);

int main() {
	int m, n;

	printf("이 프로그램은 ackemann함수의 값을 계산하는 함수입니다.\n");
	printf("순서대로 A(m, n)에서 m과 n의 값을 입력해 주세요: ");
	scanf("%d %d", &m, &n);

	printf("A(%d, %d) = %d\n", m, n, ackermann(m, n));

	return 0;
}

int ackermann(int m, int n) {
	if (m == 0)
		return (n + 1);
	else if (n == 0)
		return ackermann(m - 1, 1);
	else
		return ackermann(m - 1, ackermann(m, n - 1));
}
