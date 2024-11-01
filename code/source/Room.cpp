#include "pch.h"
#include "Room.h"

void Room::add_working_doc(Doctor* doctor){
	doc = doctor;
}

void Room::add_equipment(string equip) {
	equipment.push_back(equip);
}

void Room::add_nurse(Nurse* nurse) {
	nurses.push_back(nurse);
}

bool Room::exist_equipment(string equip){
	for (auto &eq : equipment) {
		if (eq == equip) return true;
	}
	return false;
}

Room::Room(string specialization, string equip) : specialization(specialization) {
	equipment.push_back(equip);
}

void Room::info() {
	cout << specialization << endl << "Используемое оборудование:"<<endl;
	for (auto eq : equipment) {
		cout << ' ' << eq << endl;
	}
	cout << "Работающий врач:"<<endl;
	doc->info();
	cout << endl;
	cout << "Работающие медсёстры:"<<endl;
	for (auto nurse : nurses) {
		nurse->info();
		cout << endl;
	}
}

string Room::get_specialization() {
	return specialization;
}