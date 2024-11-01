#include "pch.h"
#include "Doctor.h"
#include "Patient.h"
#include "Clinic.h"

void Doctor::info() {
	cout << "Имя :" << name << endl;
	cout << "Фамилия: " << surname << endl;
	cout << "Возраст: " << age << endl;
	cout << "Зарплата: " << salary << endl;
	cout << "Специальность: " << specialization << endl;
}

void Doctor::add_patient(Patient* patient, Clinic * clinic) {
	patients.push_back(patient);
	patient->add_doctor(this);
	clinic->add_patient(patient);
}

void Doctor::add_patient(Patient* patient) {
	patients.push_back(patient);
	patient->add_doctor(this);
	
}

void Doctor::show_patients() {
	for (auto patient : patients)
	{
		patient->info();
		cout << endl;
	}
}