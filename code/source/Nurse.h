#pragma once
#include "Employee.h"

class Nurse : public Employee {
protected:
	string specialization;
public:
	Nurse(string name, string surname, int age, double salary, string specialization)
		: specialization(specialization), Employee(name, surname, age, salary) {}
	virtual void info() override;
};