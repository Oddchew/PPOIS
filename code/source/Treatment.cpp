#include "pch.h"
#include "Treatment.h"
#include <iostream>
void Treatment::info() {
	cout << "Для лечения необходимо: " << procedure << endl;
	cout << "Для выздооровления неообходимо повторить это" << number << "раз" << endl;
}