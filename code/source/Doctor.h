#pragma once
#include "Employee.h"
#include "Treatment.h"
class Patient;
class Clinic;

class Doctor : public Employee {
protected:
	string specialization;
	vector <Patient*> patients;
public:
	Doctor(string name, string surname, int age, double salary, string specialization)
		: specialization(specialization), Employee(name, surname, age, salary) {}
	virtual void info() override;
	void add_patient(Patient* patient, Clinic* clinic);
	void add_patient(Patient* patient);
	void show_patients();

};