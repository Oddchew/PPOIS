#include "pch.h"
#include <iostream>
#include "DateTime.h"
using namespace std;

void const DateTime::date() {
	cout << "Дата: " << day << '.' << month << '.' << year << endl;
}
void const DateTime::time() {
	cout << "Время: " << hour << ':' << minute << endl;
}

void DateTime::set_date_time() {
	cout << "Введите дату формата дд:мм:гггг" << endl;
	cin.ignore(1, '\n');
	char date[11];
	char time[6];
	while (1) {
		cin >> date;
		day = int(date[0] - 48) * 10 + int(date[1] - 48);
		month = int(date[3] - 48) * 10 + int(date[4] - 48);
		year = int(date[6] - 48) * 1000 + int(date[7] - 48) * 100 + int(date[8] - 48) * 10 + int(date[9] - 48);
		if (!cin.fail() && day < 32&& month < 13) {
			break;
		}
		cin.clear();
		cout << "Некорректный ввод \n";
		cin.ignore(5475785, '\n');
	}
	cout << "Введите время формата чч:мм" << endl;
	while (1) {
		cin >> time;
		hour = int(time[0] - 48) * 10 + int(time[1] - 48);
		minute = int(time[3] - 48) * 10 + int(time[4] - 48);
		if (!cin.fail() && hour < 24 && minute < 60) {
			break;
		}
		cin.clear();
		cout << "Некорректный ввод \n";
		cin.ignore(5475785, '\n');
	}
}