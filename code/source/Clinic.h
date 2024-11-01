#pragma once
#include <vector>
#include "Patient.h"
#include "Registry.h"
#include "Room.h"
#include "Pharmacy.h"
#include "Appointment.h"
#include "Prescription.h"

class Clinic{
private:
	string name_of_clinik;
	vector <Doctor*> doctors;
	vector <Patient*> patients;
	vector <Nurse*> nurses;
	vector <Room*> rooms;
	Registry* registry;
public:
	Pharmacy* pharm;
	vector<Appointment*> appointments;
	vector<Prescription*> prescriptions;
	Clinic(string name_clin, string name_reg, string surname_reg, int age_reg, double salary_reg,
		string name_ph, string surname_ph, int age_ph, double salary_ph);

	~Clinic();

	void show_all_doctors();
	void show_all_patients();
	void show_all_nurses();
	void show_all_rooms();
	void show_all_appointments();
	void show_all_prescriptions();

	void add_doctor(Doctor* doctor);
	void add_patient(Patient* patient);
	void add_nurse(Nurse* nurse);
	void add_room(Room* room); 

	void kill();

	void patient_dead(string name, string surname);

	Doctor* get_doctor(string name, string surname);
	Patient* get_patient(string name, string surname);
	Room* get_room(string specialization);
};