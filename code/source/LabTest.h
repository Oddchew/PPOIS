#pragma once
#include <string>
#include "DateTime.h"
using namespace std;

class LabTest {
private:
    string type_of_test;
    DateTime* date;
    string result;
public:
    LabTest(string type_of_test, DateTime* date)
        : type_of_test(type_of_test), date(date) {
        set_result();
    }
    void info();
    void set_result();
    string get_result();
};