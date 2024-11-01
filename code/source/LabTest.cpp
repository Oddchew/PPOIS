#include "pch.h"
#include "LabTest.h"
#include <iostream>

void LabTest::info(){
	cout << "Тип теста: " << type_of_test << endl;
	date->date();
	date->time();
}

void LabTest::set_result() {
	srand(date->day * date->minute + date->year * date->hour);
	unsigned int change = rand() % 1000;
	if (change < 750) result = "good";
	else {
		if (change < 950) result = "normal";
		else result = "bad";
	}
}

string LabTest::get_result() {
	return result;
}