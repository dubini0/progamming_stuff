//https://dokhakdubini.tistory.com/196?category=847037

#include <stdio.h>

void powerset(char list[], int n, int len);

int main() {
	char list[] = { 'a', 'b', 'c', 'd' };
	int i;
	int len = sizeof(list) / sizeof(char);

	printf("{ ");

	for (i = 0; i < len; i++) {
		printf("%c ", list[i]);
	}

	printf("}");

	printf("의 멱급수는 다음과 같습니다: \n");

	powerset(list, -1, len);

	return 0;
}

void powerset(char list[], int n, int len) {
	int i, j;

	if (n == -1) {
		printf("{} ");
		powerset(list, 1, len);
	}
	else if (n == 1) {
		for (i = 0; i < len; i++) {
			printf("{ %c }", list[i]);
		}
		powerset(list, n + 1, len);
	}
	else if (n == len) {
		printf("{ ");
		for (i = 0; i < len; i++) {
			printf("%c ", list[i]);
		}
		printf("}");
		printf("\n");
	}
	else {
		for (i = 0; i < len; i++) {
			printf("{ ");
			for (j = 0; j < n; j++) {
				printf("%c ", list[(i + j) % len]);
			}
			printf("}");
		}

		powerset(list, n + 1, len);
	}
}
