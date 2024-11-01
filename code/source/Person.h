#pragma once
#include <string>
#include <vector>
#include <iostream>
using namespace std;

class Person {
protected:
	string name;
	string surname;
	int age;
public:
	Person(string name, string surname,int age) :name(name), surname(surname), age(age) {}
	virtual void info();
	string get_name();
	string get_surname();
};
