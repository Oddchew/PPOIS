#include "pch.h"
#include "Pharmacy.h"
#include <iomanip>

void Pharmacy::add_drug(double price, string name) {
	drugs.emplace_back(price, name);
}

Pharmacy::Pharmacy(string name, string surname, int age, double salary) {
	pharmacist = new Employee(name, surname, age, salary);
}

Pharmacy::~Pharmacy() {
	delete pharmacist;
}

void Pharmacy::info() {
	cout << left << setw(7) << "Цена" << setw(15) << "Название" << endl;
	for (auto drug : drugs) {
		cout << left << setw(7) << drug.first << setw(15) << drug.second << endl;
	}
}

double Pharmacy::get_drug(string name) {
	for (auto drug : drugs) {
		if (drug.second == name) {
			return drug.first;
		}
	}
	return -1;
}
