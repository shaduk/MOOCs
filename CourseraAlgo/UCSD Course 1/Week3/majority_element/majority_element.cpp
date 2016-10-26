#include <algorithm>
#include <iostream>
#include <vector>

using std::vector;

int get_majority_element(vector<int> &a, int left, int right) {
  if (left == right) return -1;
  if (left + 1 == right) return a[left];
  int mid = (left + right)/2;
  int ML = get_majority_element(a, left, mid);
  int MR = get_majority_element(a, mid, right);
  int c1 = 0, c2 = 0;
  for(int i = left; i < right; i++)
  {
    if(ML == a[i])
    c1++;
  }
  
  if(c1 > (right - left)/ 2)
  return ML;
  
  for(int i = left; i < right; i++)
  {
    if(MR == a[i])
    c2++;
  }
  
  if(c2 > (right - left)/ 2)
  return MR;
  
  return -1;
}

int main() {
  int n;
  std::cin >> n;
  vector<int> a(n);
  for (size_t i = 0; i < a.size(); ++i) {
    std::cin >> a[i];
  }
  std::cout << (get_majority_element(a, 0, a.size()) != -1) << '\n';
}
