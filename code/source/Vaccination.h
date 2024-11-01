#pragma once
#include <string>
#include "DateTime.h"
#include "Doctor.h"

using namespace std;

class Vaccination {
private:
	string type;
	DateTime* time;
	Doctor* doctor;
public:
	Vaccination(string type, DateTime* time, Doctor* doctor):
		type(type), time(time), doctor(doctor){}
	void info();
};