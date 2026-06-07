#include <iostream>
#include <vector>
#include <string>
using namespace std;

// Simple Student Management System using OOP + STL
class Student {
public:
    int id;
    string name;
    float marks;
    
    Student(int i, string n, float m) {
        id = i;
        name = n;
        marks = m;
    }
    
    void display() {
        cout << "ID: " << id << " | Name: " << name << " | Marks: " << marks << endl;
    }
};

int main() {
    vector<Student> students;
    
    // Adding students
    students.push_back(Student(101, "Keerthi", 89.5));
    students.push_back(Student(102, "Rahul", 92.0));
    students.push_back(Student(103, "Priya", 85.5));
    
    cout << "=== Student Management System ===" << endl;
    for(auto &s : students) {
        s.display();
    }
    
    return 0;
