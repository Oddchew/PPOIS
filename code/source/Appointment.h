#pragma once
#include "Doctor.h"
#include "Patient.h"
#include "Room.h"
#include "DateTime.h"

class Appointment {
private:
	int indf;
	Doctor* doctor;
	Patient* patient;
	Room* office;
	DateTime* time_of_app;
	bool status;
public:
	Appointment(Doctor* doc, Patient* pat, Room* off, DateTime* date_time);
	void cancel();
	void info();
};