// blog post: https://dokhakdubini.tistory.com/172?category=847037

#include <stdio.h>
#define swap(a, b, tmp){(tmp) = (a); (a) = (b); (b) = (tmp);}

void selec_sort(int *list, int n);

int main() {
	int n, *list;

	printf("배열의 크기는? ");
	scanf(" %d", &n);

	//malloc으로 동적할당을 해준 모습인데, 이는 list를 동적할당해주기 위함이고
	//동적할당을 쓰지 않으시려면 그냥 list를 큰값으로 설정해주시면 됩니다. ex) list[100]
	list = malloc(sizeof(int) * n);

	for (int i = 0; i < n; i++) {
		printf("%d번째 숫자를 입력해주세요: ", i + 1);
		scanf("%d", &list[i]);
	}
	/*for (int i = 0; i < n; i++) {
		printf(" %d", list[i]);
	}*/

	selec_sort(list, n);
}

void selec_sort(int *list, int n) {
	int i, j, tmp;
	int min;

	for (i = 0; i < n; i++) {
		min = i;
		for (j = i; j < n; j++) {
			if (list[min] > list[j]) {
				min = j;
			}
		}
		swap(list[min], list[i], tmp);
	}

	printf("정렬된 배열: ");
	for (i = 0; i < n; i++) {
		printf("%d ", list[i]);
	}
}
