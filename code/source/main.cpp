#include "Clinic.h"
#include <conio.h>
#include <fstream>

int static input() {
	unsigned int n;
	while (1) {
		cin >> n;
		if (!cin.fail()){
			if(n<=17) break;
		}
		cin.clear();
		cout << "Некорректный ввод \n";
		cin.ignore(5475785, '\n');
	}
	return n;
}

string static input_str() {
	string str;
	cin >> str;
	return str;
}

string const static path = "pharm.p";
void static add_grugs_file(string path, Pharmacy* pharm) {
	ifstream fin(path);
	if (!fin.is_open()) {
		cout << "Такого файла не существует";
		return;
	}
	string name;
	double price;

	while (fin >> name >> price) {
		pharm->add_drug(price,name);
	}
}

int static menu() {
	int n;
	cout << "Введите цифру необходимой операции:\n";
	cout << " 1.Вывод всех врачей\n";
	cout << " 2.Вывод всех медсестер\n";
	cout << " 3.Вывод всех пациентов\n";
	cout << " 4.Вывод всех кабинетов\n";
	cout << " 5.Вывод всех записей на прием\n";
	cout << " 6.Вывод всех рецептов\n";
	cout << " 7.Добавление нового пациента\n";
	cout << " 8.Запись на прием к врачу\n";
	cout << " 9.Сдача анализов\n";
	cout << " 10.Трудоустройство нового врача\n";
	cout << " 11.Трудоустройство новой медсестры\n";
	cout << " 12.Постройка нового кабинета\n";
	cout << " 13.Добавление нового оборудования\n";
	cout << " 14.Пройти вакцинацию\n";
	cout << " 15.Лечение пациента\n";
	cout << " 16.Выписать рецепт\n";
	cout << " 17.Завершить работу\n";
	n = input();
	return n;
}

int main()
{
	system("chcp 1251 > nul");
	Clinic A("Поликлиника города Минска №1", "Иванова", "Елена", 44, 3290.35, "Зинаида", "Ефимец",58,1293);
	add_grugs_file(path, A.pharm);

	Doctor B1("Александр","Авсейков",28,2395.35,"Хирург"), B2("Светлана", "Игнатьева", 38, 1855.35, "Невролог"), 
		B3("Татьяна", "Менчицкая", 58, 1885.35, "Врач общей практики"),B4("Ювеналий", "Игонин", 45, 2025.35, "Онколог"), 
		B5("Дмитрий", "Антилевский", 27, 2045.35, "Стоматолог"), B6("Денис", "Богачев", 42, 1815.35, "Рентгенолог");

	Nurse C1("Ольга", "Волкова", 28, 1034.4, "хирургия"), C2("Елена", "Антапова", 32, 1034.4, "Неврология"),
		C3("Анастасия", "Чумакова", 29, 1034.4, "Общая практика"), C4("Анастасия", "Чумакова", 44, 1034.4, "Стоматология"),
		C5("Арина", "Гаврилова", 51, 1034.4, "Онкология"), C6("Анастасия", "Чумакова", 39, 1034.4, "Рентгенология");

	Room D1("Кабинет хирурга", "хирургический стол"), D2("Кабинет невролога", "неврологический молоточек"),
		D3("Кабинет врача общей практики", "тонометр"), D4("Кабинет онколога", "Весы"),
		D5("Кабинет стоматолога", "стоматологическое кресло"), D6("Кабинет рентгенолога", "рентген-аппарат");

	Patient E1("Вероника", "Лукина", 20, "аппендицит"), E2("Алексей", "Мальцев", 31, "внутренний перелом лучевой кости"),
		E3("Василиса", "Кольцева", 42, "эпилепсия"), E4("Владислав", "Коммисаров", 24, "панические атаки"),
		E5("Алексей", "Масленников", 51, "грипп"), E6("Тихон", "Савельев", 12, "ОРВИ"),
		E7("Тимофей", "Калинин", 72, "рак легких"), E8("Артемий", "Егоров", 88, "лейкемия"),
		E9("Есения", "Макарова", 36, "пульпит"), E10("Виктория", "Мельникова", 16, "кариес");

	A.add_doctor(&B1);
	A.add_doctor(&B2);
	A.add_doctor(&B3);
	A.add_doctor(&B4);
	A.add_doctor(&B5);
	A.add_doctor(&B6);

	A.add_nurse(&C1);
	A.add_nurse(&C2);
	A.add_nurse(&C3);
	A.add_nurse(&C4);
	A.add_nurse(&C5);
	A.add_nurse(&C6);

	D1.add_working_doc(&B1);
	D1.add_nurse(&C1);
	D2.add_working_doc(&B2);
	D2.add_nurse(&C2);
	D3.add_working_doc(&B3);
	D3.add_nurse(&C3);
	D4.add_working_doc(&B4);
	D4.add_nurse(&C5);
	D5.add_working_doc(&B5);
	D5.add_nurse(&C4);
	D6.add_working_doc(&B6);
	D6.add_nurse(&C6);

	A.add_room(&D1);
	A.add_room(&D2);
	A.add_room(&D3);
	A.add_room(&D4);
	A.add_room(&D5);
	A.add_room(&D6);

	B1.add_patient(&E1, &A);
	B1.add_patient(&E2, &A);
	B2.add_patient(&E3, &A);
	B2.add_patient(&E4, &A);
	B3.add_patient(&E5, &A);
	B3.add_patient(&E6, &A);
	B4.add_patient(&E7, &A);
	B4.add_patient(&E8, &A);
	B5.add_patient(&E9, &A);
	B5.add_patient(&E10, &A);

	//A.patient_dead("Тимофей", "Калинин");
	int n = 0;
	while (n != 17) {
		n = menu();
		string name, surname, disease, test_name, specialization,equipment,type_vaccine, procedure;
		double salary;
		int age, number;
		Patient* pat;
		Doctor* doc;
		Nurse* nur;
		Room* office;
		Appointment* app;
		DateTime* date_and_time;
		LabTest* test;
		switch (n) {
		case 1:
			system("cls");
			A.show_all_doctors();
			break;
		case 2:
			system("cls");
			A.show_all_nurses();
			break;
		case 3:
			system("cls");
			A.show_all_patients();
			break;
		case 4:
			system("cls");
			A.show_all_rooms();
			break;
		case 5:
			system("cls");
			A.show_all_appointments();
			break;
		case 6:
			system("cls");
			A.show_all_prescriptions();
			break;
		case 7:
			system("cls");
			cout << "Введите имя пациента" << endl;
			cin >> name;
			cout << "Введите фамилию пациента" << endl;
			cin >> surname;
			cout << "Введите возраст пациента" << endl;
			cin >> age;
			cout << "Введите болезнь пациента" << endl;
			cin.clear();
			cin.ignore();
			getline(cin, disease);
			pat = new Patient(name, surname, age, disease);
			system("cls");
			A.show_all_doctors();
			do {
				cout << "Введите имя врача, который будет лечить пациента" << endl;
				cin >> name;
				cout << "Введите фамилию врача, который будет лечить пациента" << endl;
				cin >> surname;
				doc = A.get_doctor(name, surname);
			} while (doc == nullptr);
			doc->add_patient(pat, &A);
			break;
		case 8:
			system("cls");
			A.show_all_patients();
			do {
				cout << "Введите имя пациента" << endl;
				cin >> name;
				cout << "Введите фамилию пациента" << endl;
				cin >> surname;
				pat = A.get_patient(name, surname);
			} while (pat == nullptr);
			system("cls");
			A.show_all_doctors();
			do {
				cout << "Введите имя врача, который будет лечить пациента" << endl;
				cin >> name;
				cout << "Введите фамилию врача, который будет лечить пациента" << endl;
				cin >> surname;
				doc = A.get_doctor(name, surname);
			} while (doc == nullptr);
			system("cls");
			A.show_all_rooms();
			do {
				cout << "Введите название кабинета" << endl;
				getline(cin, name);
				office = A.get_room(name);
			} while (office == nullptr);
			system("cls");
			date_and_time = new DateTime();
			cin.clear();
			date_and_time->set_date_time();
			app = new Appointment(doc, pat, office,date_and_time);
			A.appointments.push_back(app);
			break;
		case 9:
			system("cls");
			A.show_all_patients();
			cout << "Настало время сдавать анализы" << endl;
			do {
				cout << "Введите имя пациента" << endl;
				cin >> name;
				cout << "Введите фамилию пациента" << endl;
				cin >> surname;
				pat = A.get_patient(name, surname);
			} while (pat == nullptr);
			cout << "Введите показатель, который будет проверяться" << endl;
			cin.clear();
			cin.ignore();
			getline(cin, test_name);

			date_and_time = new DateTime();
			date_and_time->set_date_time();
			test = new LabTest(test_name, date_and_time);
			pat->tests.push_back(test);
			break;
		case 10:
			system("cls");
			cout << "Введите имя врача" << endl;
			cin >> name;
			cout << "Введите фамилию врача" << endl;
			cin >> surname;
			cout << "Введите возраст врача" << endl;
			cin >> age;
			cout << "Введите специализацию врача" << endl;
			getline(cin, disease);
			cout << "Введите зарплату врача" << endl;
			cin >> salary;
			doc = new Doctor(name, surname, age, salary,specialization);
			A.add_doctor(doc);

			A.show_all_rooms();
			cout << "В каком кабинете доктор будет работать?" << endl;
			do {
				cout << "Введите название кабинета" << endl;
				getline(cin, name);
				office = A.get_room(name);
			} while (office == nullptr);
			office->add_working_doc(doc);
			break;
		case 11:
			system("cls");
			cout << "Введите имя медсестры" << endl;
			cin >> name;
			cout << "Введите фамилию медсестры" << endl;
			cin >> surname;
			cout << "Введите возраст медсестры" << endl;
			cin >> age;
			cout << "Введите специализацию медсестры" << endl;
			getline(cin, disease);
			cout << "Введите зарплату медсестры" << endl;
			cin >> salary;
			nur = new Nurse(name, surname, age, salary, specialization);
			A.add_nurse(nur);

			A.show_all_rooms();
			cout << "В каком кабинете медсестра будет работать?" << endl;
			do {
				cout << "Введите название кабинета" << endl;
				getline(cin, name);
				office = A.get_room(name);
			} while (office == nullptr);
			office->add_nurse(nur);
			break;
		case 12:
			system("cls");
			cout << "Введите какой специализации будет этот кабинет" << endl;
			getline(cin, specialization);
			cout << "Введите используемое оборудование" << endl;
			getline(cin, equipment);
			office = new Room(specialization,equipment);
			A.add_room(office);
			break;
		case 13:
			system("cls");
			A.show_all_rooms();
			cout << "Введите в какой кабинет вы хотите добавить оборудование" << endl;
			cin.clear();
			cin.ignore();
			do {
				getline(cin, specialization);
				office = A.get_room(specialization);
			} while (office == nullptr);
			cout << "Введите название оборудования" << endl;
			getline(cin, equipment);
			office->add_equipment(equipment);
			break;
		case 14:
			system("cls");
			A.show_all_patients();
			cout << "Кого будем вакцинировать?\n";
			do {
				cout << "Введите имя пациента" << endl;
				cin >> name;
				cout << "Введите фамилию пациента" << endl;
				cin >> surname;
				pat = A.get_patient(name, surname);
			} while (pat == nullptr);

			system("cls");
			A.show_all_doctors();
			do {
				cout << "Введите имя врача, который будет вакцинировать пациента" << endl;
				cin >> name;
				cout << "Введите фамилию врача, который будет вакцинировать пациента" << endl;
				cin >> surname;
				doc = A.get_doctor(name, surname);
			} while (doc == nullptr);

			date_and_time = new DateTime();
			date_and_time->set_date_time();

			cout << "Введите болезнь от которой ставится вакцина\n" << endl;
			cin.clear();
			cin.ignore();
			getline(cin, type_vaccine);

			pat->vaccin = new Vaccination(type_vaccine, date_and_time, doc);
			pat->vaccin->info();
			break;
		case 15:
			system("cls");

			A.show_all_patients();
			cout << "Кого будем лечить?\n";
			do {
				cout << "Введите имя пациента" << endl;
				cin >> name;
				cout << "Введите фамилию пациента" << endl;
				cin >> surname;
				pat = A.get_patient(name, surname);
			} while (pat == nullptr);

			cout << "Что пациенту необходимо принимать или делать?\n" << endl;
			cin.clear();
			cin.ignore();
			getline(cin, procedure);
			cout << "Введите количество повторений" << endl;
			cin >> number;
			pat->add_treat(procedure, number);
			pat->treat->info();
			break;
		case 16:
			system("cls");

			A.show_all_patients();
			cout << "Кому выписать рецепт?\n";
			do {
				cout << "Введите имя пациента" << endl;
				cin >> name;
				cout << "Введите фамилию пациента" << endl;
				cin >> surname;
				pat = A.get_patient(name, surname);
			} while (pat == nullptr);

			system("cls");
			A.show_all_doctors();
			do {
				cout << "Введите имя врача, который выписывает рецепт" << endl;
				cin >> name;
				cout << "Введите фамилию врача, который выписывает рецепт" << endl;
				cin >> surname;
				doc = A.get_doctor(name, surname);
			} while (doc == nullptr);
			
			cout << "Какое лекарство пациенту нужно принимать" << endl;
			cin.clear();
			cin.ignore();
			getline(cin, name);
			Prescription* prescr = new Prescription();
			prescr->add_prescription(doc, pat, name);
			A.prescriptions.push_back(prescr);
			break;
		}
		A.kill();
		cout << "Для продолжения нажмите любую клавишу\n";
		_getch();
		system("cls");
	}
}

/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
///////////////////   Запуск тестов OpenCppCoverage --source PPOIS2 -- .\x64\Debug\Test_PPOIS2.exe   ///////////////////////////
///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////