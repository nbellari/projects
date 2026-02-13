#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv) {
  int n, num;
  long sum;

  cin >> n;
  for (int i = 1; i <= n; i++) {
    cin >> num;
    sum = 0;
    while (num) {
      sum += num % 10;
      num /= 10;
    }
    cout << sum << endl;
  }
  return 0;
}