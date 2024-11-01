#pragma once
#include <vector>
#include <string>
#include <utility>
#include "Employee.h"
using namespace std;

class Pharmacy{
private:
	vector <pair <double, string >> drugs;
	Employee* pharmacist;
public:
	Pharmacy(string name, string surname, int age, double salary);
	~Pharmacy();
	void add_drug(double price, string name);
	double get_drug(string name);

	void info();
};