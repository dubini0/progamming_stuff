#include <stdio.h>
#include <stdlib.h>
#include <time.h>
 
#define MAX 30 // 배열의 최대 크기 
#define FUN(x) (x*x - 100*x + 8) // 임의의 함수 정의

int find(int result, int n);
 
int output[MAX] = { 0 }; // 각 변수의 함수결과값 저장
int inputs[MAX] = { 0 }; // 함수에서 계산된 변수 저장
 
void main()
{
  int i, equal; // equal: 같은 함수값이 있는지 확인하는 변수
  int num, count = 0; // num: random으로 생성하는 입력값, count: 단순 카운팅 변수
  int val, result; // val: 같은 함수값을 갖는 이전 입력값
 
  srand((unsigned)time(NULL));
  while (count < MAX)
  {
    equal = 0;
    num = (int)((double)rand() / RAND_MAX * 100); // 0~99 난수 생성
 
    // 이미 사용된 입력값인지 확인한다. 우리는 같은 출력값을 가지는 다른 입력 둘을 찾고 있다.
    for (i = 0; i < count; i++)
      if (inputs[i] == num) // 기존의 입력값 배열에 내가 입력하려는 값이 있는지 확인한다.
      {
        equal = 1;
        break;
      }
    if (equal) // 같은 값이 있다면 while문의 처음으로
      continue;
 
    result = FUN(num); // 함수에 num을 대입한 결과값 저장
 
    // n개보다 작은 결과값, 즉 같은 결과값이 있다면 value를 리턴하고
    // 없다면 -1 리턴
    if ((val = find(result, count)) == -1) { // val에는 -1 또는 values[i] 값이 담긴다. (이전 입력값)
      output[count] = result; // 결과값을 배열에 저장
      inputs[count++] = num; // 변수를 배열에 저장
    }
    else {
      printf("a = %d, b = %d\n", val, num); // val: 같은 함수값을 갖는 이전 입력값, num: 현재 입력값
      break;
    }
  }
}
 
int find(int result, int n)
{
  int i;
  for (i = 0; i < n; i++)
    if (result == output[i])
      return inputs[i]; // 그 값을 찾은 경우 전의 입력값을 리턴한다.
  return -1; // 찾는 값이 없을 경우
}
