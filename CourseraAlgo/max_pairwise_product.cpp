#include <iostream>
#include <vector>

using std::vector;
using std::cin;
using std::cout;

long long MaxPairwiseProduct(const vector<int>& numbers) {
  long long result = 0;
  int a = -1, b = -1;
  int n = numbers.size();
  for (int i = 0; i < n; ++i) {
        if((a == -1) || (numbers[i] > numbers[a]))
        a = i;
    }
    
  for (int i = 0; i < n; ++i) {
        if((i != a) && ((b == -1) || (numbers[i] > numbers[b])))
        b = i;
    }
  
  result = numbers[a]*numbers[b];
  return result;
}

int main() {
    int n;
    cin >> n;
    vector<int> numbers(n);
    for (int i = 0; i < n; ++i) {
        cin >> numbers[i];
    }

    int result = MaxPairwiseProduct(numbers);
    cout << result << "\n";
    return 0;
}
