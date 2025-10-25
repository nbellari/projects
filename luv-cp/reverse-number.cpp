#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv) {
  int n, num, rnum;

  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> num;
    rnum = 0;
    while (num) {
      rnum = (rnum * 10) + (num % 10);
      num /= 10;
    }
    cout << rnum << endl;
  }
  return 0;
}