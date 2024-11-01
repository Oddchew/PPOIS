#include "pch.h"
#include "Vaccination.h"

void Vaccination::info() {
	cout << "Доктор проводивший вакцинацию:" << endl;
	doctor->info();
	cout << "Тип вакцины:" << endl;
	cout << type << endl;
	time->date();
	time->time();
}