#pragma once
#include <vector>
#include "Patient.h"

class MedicalRecord {
private:
	Patient* patient;
	vector <string> medical_history;
public:
	MedicalRecord(Patient* patient) : patient(patient) {}
	void add_rec(string record);
	void check_history();
};