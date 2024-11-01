#pragma once
#include "Employee.h"
#include "MedicalRecord.h"
class Registry {
private:
	Employee employee;
public:
	vector <MedicalRecord*> records;
	Registry(string name_em, string surname_em, int age_em, double salary_em) : employee(name_em, surname_em, age_em, salary_em) {}
	void add_record(MedicalRecord* rec);
};