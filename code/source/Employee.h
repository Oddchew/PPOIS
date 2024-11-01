#pragma once
#include "Person.h"

class Employee : public Person {
protected:
	double salary;
public:
	Employee(string name, string surname, int age, double salary) : salary(salary), Person(name, surname, age) {}
	virtual void info() override;
};