#include <bits/stdc++.h>

using std::cout;
using std::endl;

class GradeBook {
public:
  void displayMessage() { cout << "Grade Book Message!" << endl; }
};

int main() {
  GradeBook myGradeBook;
  myGradeBook.displayMessage();

  return 0;
}