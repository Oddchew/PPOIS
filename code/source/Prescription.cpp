#include "pch.h"
#include "Prescription.h"

void Prescription::add_prescription(Doctor* doc, Patient* patient1, string name_of_medicament) {
	doctor = doc;
	patient = patient1;
	name_of_med = name_of_medicament;
}

void Prescription::show() {
	cout << "Врач, выписавший рецепт";
	doctor->info();
	cout << endl;
	cout << "Пициент";
	patient->info();
	cout << endl;
	cout << "Название лекарства: " << name_of_med << endl;
}