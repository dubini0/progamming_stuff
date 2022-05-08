//https://dokhakdubini.tistory.com/82?category=814319
//05_10에서 깊은복사까지 추가한 코드임

#include <iostream>
#include <cstring>
using namespace std;

class Person {
	char* name;
	int id;
public:
	Person(int id, const char* name);
	Person(Person& p);
	~Person();
	void changeName(const char *name);
	void show() { cout << id << ',' << name << endl; }
};

Person::Person(Person& p) {
	this->id = p.id;
	int len = strlen(p.name);
	this->name = new char[len+1];
	strcpy(this->name, p.name);
	cout << "복사 생성자 실행. 원본 객체의 이름" << this->name << endl;
}

Person::Person(int id, const char* name) {
	this->id = id;
	int len = strlen(name);
	this->name = new char[len + 1];
	//이름을 바로 복사하는게 아니라 일단 공간을 할당하고, 그 뒤에 복사해주기
	strcpy(this->name, name);
	cout <<this->name << " 생성자 실행" << endl;
}

void Person::changeName(const char* name) {
	/*if (strlen(name) > strlen(this->name))
		return;*/
		//이거는 메모리 문제때문에 아예 막아놓음
	if (this->name) {
		delete[] this->name;
		this->name = NULL;
	}
	this->name = new char[strlen(name) + 1];
	strcpy(this->name, name);
}

Person::~Person() {
	cout << this->name << " 생성자 소멸" << endl;
	if (name) {
		delete[] name;
		name = NULL;
	}
}

int main() {
	Person father(1, "Kitae");			// (1) father 객체 생성
	Person daughter(father);			// (2) daughter 객체 복사 생성. 복사생성자호출

	cout << "daughter 객체 생성 직후 ----" << endl;
	father.show();						// (3) father 객체 출력
	daughter.show();					// (3) daughter 객체 출력

	daughter.changeName("Grace"); // (4) daughter의 이름을 "Grace"로 변경
	cout << "daughter 이름을 Grace로 변경한 후 ----" << endl;
	father.show();						// (5) father 객체 출력
	daughter.show();					// (5) daughter 객체 출력

	return 0;								// (6), (7) daughter, father 객체 소멸
}
