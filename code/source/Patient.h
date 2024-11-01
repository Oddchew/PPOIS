#pragma once
#include "Person.h"
#include "Treatment.h"
#include "LabTest.h"
#include "Vaccination.h"
class Doctor;

class Patient : protected Person {
protected:
	string disease;
	vector <Doctor*> doctors;
public:
	Treatment *treat = nullptr;
	vector <LabTest*> tests;
	Vaccination* vaccin;
	Patient(string name, string surname, int age, string disease) : disease(disease), Person(name, surname, age),vaccin(nullptr) {}
	virtual void info() override;
	string get_name() const;
	string get_surname() const;
	string get_disaese() const;
	void add_doctor(Doctor* doctor);
	void show_doctors();
	void add_treat(string procedure, int number);
};