#include "pch.h"
#include "MedicalRecord.h"

void MedicalRecord::add_rec(string record) {
	medical_history.push_back(record);
}

void MedicalRecord::check_history()
{
	cout << "Медицинская история " << patient->get_name() << ' ' << patient->get_surname() << endl;
	for (auto &rec : medical_history)
	{
		cout << "- " << rec << endl;
	}
}