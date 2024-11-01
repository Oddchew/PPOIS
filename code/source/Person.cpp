#include "pch.h"
#include "Person.h"

void Person::info(){
	cout << "Имя :" << name << endl;
	cout << "Фамилия: " << surname << endl;
	cout << "Возраст: " << age << endl;
}

string Person::get_name() {
	return name;
}

string Person::get_surname() {
	return surname;
}