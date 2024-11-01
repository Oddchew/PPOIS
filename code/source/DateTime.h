#pragma once

struct DateTime {
	unsigned int day;
	unsigned int month;
	int year;
	unsigned int hour;
	unsigned int minute;

	void const date();
	void const time();

	DateTime(unsigned int day, unsigned int month, int year, unsigned int hour, unsigned int minute)
		: day(day), month(month), year(year), hour(hour), minute(minute) {}  

	DateTime() {}

	void set_date_time();
};