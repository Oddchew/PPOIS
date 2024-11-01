#include "pch.h"
#include "Clinic.h"

Clinic::Clinic(string name_clin, string name_reg, string surname_reg, int age_reg, double salary_reg,
	string name_ph, string surname_ph, int age_ph, double salary_ph)
	: name_of_clinik(name_clin) {
	registry = new Registry(name_reg, surname_reg, age_reg, salary_reg);
	pharm = new Pharmacy(name_ph, surname_ph, age_ph, salary_ph);
}

Clinic::~Clinic() {
	delete registry; 
	delete pharm;
}

void Clinic::show_all_doctors(){
	for (auto &doc : doctors){
		doc->info();
		cout << endl;
	}
}

void Clinic::show_all_patients() {
	for (auto  &patient : patients) {
		patient->info();
		cout << endl;
	}
}

void Clinic::show_all_nurses() {
	for (auto& nurse : nurses) {
		nurse->info();
		cout << endl;
	}
}

void Clinic::show_all_rooms() {
	for (auto& room : rooms) {
		room->info();
		cout << endl;
	}
}

void Clinic::show_all_appointments() {
	for (auto& app : appointments) {
		app->info();
		cout << endl;
	}
}

void Clinic::show_all_prescriptions() {
	for (auto rec : registry->records) {
		rec->check_history();
	}
}

void Clinic::add_doctor(Doctor* doctor) {
	doctors.push_back(doctor);
}
void Clinic::add_patient(Patient* patient) {
	for (auto pat : patients) {
		if (pat == patient) return;
	}
	patients.push_back(patient);
}
void Clinic::add_nurse(Nurse* nurse) {
	nurses.push_back(nurse);
}
void Clinic::add_room(Room* room) {
	rooms.push_back(room);
}

Doctor* Clinic::get_doctor(string name, string surname) {
	for (auto doc : doctors) {
		if (doc->get_name() == name && doc->get_surname() == surname) {
			return doc;
		}
	}
	cout << "Такого врача нет" << endl;
	return nullptr;
}

Patient* Clinic::get_patient(string name, string surname) {
	for (auto patient : patients) {
		if (patient->get_name() == name && patient->get_surname() == surname) {
			return patient;
		}
	}
	cout << "Такого пациента нет" << endl;
	return nullptr;
}

Room* Clinic::get_room(string specialization) {
	for (auto room : rooms) {
		if (room->get_specialization() == specialization) {
			return room;
		}
	}
	cout << "Такого кабинета нет" << endl;
	return nullptr;
}

void Clinic::patient_dead(string name, string surname) {
	for (int i = 0; i < patients.size(); ++i) {
		if (patients[i]->get_name() == name && patients[i]->get_surname() == surname) {
			system("cls");
			cout << "В связи с тяжелым состоянием пациент " << name << ' ' << surname << " умер от " << patients[i]->get_disaese() <<endl;               
			patients.erase(patients.begin() + i); 
			break;                           
		}
	}
}

void Clinic::kill() {
	int i = 0;
	for (auto pat : patients)
	{
		for (auto test: pat->tests) {
			i++;
			int k;

			if (pat->vaccin != nullptr) k = 0.2;
			else k = 1;

			if (test->get_result() == "good") {
				srand(i);
				if (int(((rand()+1111) % 1000) / k) == 520) {
					patient_dead(pat->get_name(), pat->get_surname());
				}
			}

			if (test->get_result() == "normal") {
				srand(i);
				if (int(((rand() + 111) % 100) / k) == 65) {
					patient_dead(pat->get_name(), pat->get_surname());
				}
			}

			if (test->get_result() == "bad") {
				srand(i);
				if (int(((rand() + 11) % 10) / k) == 5|| int(((rand() + 11) % 10) / k) == 2 || int(((rand() + 11) % 10) / k) == 0) {
					patient_dead(pat->get_name(), pat->get_surname());
				}
			}
		}
	}
}