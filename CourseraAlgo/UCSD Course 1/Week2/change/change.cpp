#include <iostream>

int get_change(int n) {
  int total = n, ans = 0;
  while(total)
  {
    if(total >= 10)
    {
      total = total - 10;
      ans++;
    }
    else if(total >= 5)
    {
      total = total-5;
      ans++;
    }
    else
    {
      total = total-1;
      ans++;
    }
  }
  return ans;
}

int main() {
  int n;
  std::cin >> n;
  std::cout << get_change(n) << '\n';
}
