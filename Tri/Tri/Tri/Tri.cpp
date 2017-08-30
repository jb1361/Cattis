// Tri.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
#include <list>
#include <sstream>
using namespace std;
list<string> output;
void compute(int data[]);
void print_output();

int main()
{
	int temp[3];
	string str;
	getline(cin, str);
	int j = 0;
	for (int i = 0; i<str.length(); ++i)
	{
		if (str[i] != ' ') {
			stringstream ss;
			string target;
			char mychar = str[i];
			ss << mychar;
			for (int k = i; k < str.length(); k++) {
				if (str[k + 1] != ' ') {
					ss << str[k + 1];
					i++;
				}
				else break;
			}
		
			target = ss.str();
			
			int tempi = stoi(target);
			temp[j] = tempi;
			j++;
		}
	}
	
	compute(temp);
	return 0;
}


void compute(int data[]) {	
	

	
	int eq_first = data[0];
	int middle = data[1];
	int eq_last = data[2];

	//cout << "first: " << eq_first << " middle: " << middle <<  " last: " << eq_last << "\n";
	
	stringstream ss;
	ss << eq_first;
	string first = ss.str();
	stringstream ss1;
	ss1 << middle;
	string mid = ss1.str();
	stringstream ss2;
	ss2 << eq_last;
	string last = ss2.str();
	
	
	//I know the ss ss1 ss2 are bad but this has taken too long
	if (eq_first + middle == eq_last) {
		string out = first + '+' + mid + '=' + last;
		output.insert(output.end(),out);
		return print_output();
	}
	else if (eq_first - middle == eq_last) {
		string out = first + '-' + mid + '=' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (eq_first * middle == eq_last) {
		string out = first + '*' + mid + '=' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (eq_first / middle == eq_last) {
		string out = first + '/' + mid + '=' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (middle + eq_last == eq_first) {
		string out = first + '=' + mid + '+' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (middle - eq_last == eq_first) {
		string out = first + '=' + mid + '-' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (middle * eq_last == eq_first) {
		string out = first + '=' + mid + '*' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	else if (middle / eq_last == eq_first) {
		string out = first + '=' + mid + '/' + last;
		output.insert(output.end(), out);
		return print_output();
	}
	

}

void print_output() {
	for (auto v : output) cout << v;
}