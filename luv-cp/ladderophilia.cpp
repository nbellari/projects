#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv) {
  int n;
  string ladderSide = "*   *\n*   *";

  cin >> n;
  cout << ladderSide << endl;
  for (int i = 1; i <= n; i++) {
    cout << "*****" << endl;
    cout << ladderSide << endl;
  }

  return 0;
}