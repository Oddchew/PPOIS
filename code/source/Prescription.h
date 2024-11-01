#pragma once
#include "Patient.h"
#include "Doctor.h"
class Prescription {
private:
	Doctor* doctor;
	Patient* patient;
public:
	string name_of_med;
	void add_prescription(Doctor* doctor, Patient* patient, string name_of_med);
	void show();
};