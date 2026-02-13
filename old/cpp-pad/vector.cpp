#include <iostream>

using namespace std;

class Vector {
public:
  Vector(int s) : _elem{new double[s]}, _sz(s) {}
  double operator[](int i) { return _elem[i]; }
  int size() { return _sz; }

private:
  double *_elem;
  int _sz;
};

int main() {
  Vector v(10);

  cout << "Size of v: " << v.size() << endl;
  return 0;
}