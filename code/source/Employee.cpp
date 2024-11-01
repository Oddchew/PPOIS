#include "pch.h"
#include "Employee.h"

void Employee::info() {
	cout << "Имя :" << name << endl;
	cout << "Фамилия: " << surname << endl;
	cout << "Возраст: " << age << endl;
	cout << "Зарплата: " << salary << endl;
}