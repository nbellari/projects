#include <bits/stdc++.h>

using namespace std;

string num2word(int i) {
  switch (i) {
  case 0:
    return "zero";
    break;
  case 1:
    return "one";
    break;
  case 2:
    return "two";
    break;
  case 3:
    return "three";
    break;
  case 4:
    return "four";
    break;
  case 5:
    return "five";
    break;
  case 6:
    return "six";
    break;
  case 7:
    return "seven";
    break;
  case 8:
    return "eight";
    break;
  case 9:
    return "nine";
    break;
  default:
    return "none";
    break;
  }
}

int main(int argc, char **argv) {
  int a, b;

  cin >> a >> b;
  for (int i = a; i <= b; i++) {
    if (i <= 9) {
      cout << num2word(i) << endl;
    } else if (i % 2 != 0) {
      cout << "odd" << endl;
    } else {
      cout << "even" << endl;
    }
  }
}