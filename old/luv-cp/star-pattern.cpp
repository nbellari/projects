#include <bits/stdc++.h>

using namespace std;

int main() {
  int nPatterns = 0;

  cin >> nPatterns;
  cout << "Number of Patterns:" << nPatterns << endl;

  while (nPatterns--) {
    int n;
    cin >> n;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= i; j++) {
        cout << "*";
      }
      cout << endl;
    }
  }
  return 0;
}