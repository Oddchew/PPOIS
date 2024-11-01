#include "pch.h"
#include "Registry.h"

void Registry::add_record(MedicalRecord* rec) {
	records.push_back(rec);
}