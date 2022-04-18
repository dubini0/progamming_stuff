#include <stdio.h>

//size 크기의 data배열안에서 searchnum을 찾기
//값이없으면 -1반환
//값이 있으면 data배열의 index 반환

int binarySearch(int data[], int size, int searchnum){
	int left = 0; //시작
	int right = size - 1; //끝
	int middle;
	while (left <= right) {
		middle = (left + right) / 2;
		if (data[middle] == searchnum) return middle;
		else if (data[middle] > searchnum) right = middle - 1;
		else left = middle + 1;
	}
	return -1;
}

int main() {
	int searchnum;
	int data[] = { 1,3,6,8,11,23,111,114,213 };
	int dataSize = sizeof(data) / sizeof(int);
	for (int i = 0; i < 9 ; i++) {
		printf("%d ", data[i]);
	}
	printf("\n");
	printf("찾을 숫자: ");
	scanf("%d", &searchnum);
	int ans = binarySearch(data, dataSize, searchnum);
	printf("%d번째 인덱스, 값: %d\n", ans+1, data[ans]);
}
