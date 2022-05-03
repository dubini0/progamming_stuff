// https://dokhakdubini.tistory.com/195?category=847037
#include <stdio.h>
#include <stdlib.h>

void move(int from, int to);
void hanoi(int n, int from, int to, int via);

int count=0;

int main() {
	int n;
	printf("Please input the number of disks: ");
	scanf("%d", &n);
	if (n < 1) {
		fprintf(stderr, "Please input number bigger than 0.\n");
		exit(EXIT_FAILURE);
	}

	hanoi(n, 1, 3, 2);

	printf("Thus, the mininal number of moves is %d.", count);
	return 0;
}

void hanoi(int n, int from, int to, int via) {
	if (n == 1) {
		move(from, to);
		count++;
	}
	else {
		hanoi(n - 1, from, via, to);
		move(from, to);
		count++;
		hanoi(n - 1, via, to, from);
	}
}

void move(int from, int to) {
	printf("The upmost disk in rod %d is moved to rod %d.\n", from, to);
}
