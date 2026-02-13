#include <bits/stdc++.h>

using namespace std;

int main(int argc, char **argv) {
  int n, total = 0;

  cin >> n;

  if (n % 2) {
    goto exit;
  }

  n = n / 2;

  for (int i = 1; i <= n / 2; i++) {
    if (i == (n - i)) {
      continue;
    }
    total++;
  }

exit:
  cout << total << endl;

  return 0;
}