#pragma once
#include <string>
using namespace std;

class Treatment {
private:
	string procedure;
	int number;
public:
	Treatment(string procedure, int number)
		:procedure(procedure), number(number) {}
	void info();
};