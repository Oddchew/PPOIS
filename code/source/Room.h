#pragma once
#include "Doctor.h"
#include "Nurse.h"

class Room {
private:
	string specialization;
	vector <string> equipment; //оборудование
	Doctor* doc = nullptr;
	vector <Nurse*> nurses;
public:
	Room(string specialization, string equip);
	void add_working_doc(Doctor* doctor);
	void add_equipment(string equip);
	void add_nurse(Nurse* nurse);
	bool exist_equipment(string equip);
	string get_specialization();
	void info();
};