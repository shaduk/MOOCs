#include <iostream>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;

bool cmp(pair <int,int> a, pair <int,int> b)
{
    double r1 = (double)a.first / a.second;
    double r2 = (double)b.first / b.second;
    return r1 > r2;
}

double get_optimal_value(int capacity, vector<int> weights, vector<int> values) {
  
  double value = 0.0;
  int curWeight = 0;
  vector < pair<int,int> > foo;
  
  for(int i = 0; i < weights.size(); i++)
  {
    foo.push_back(make_pair (values[i],weights[i]));
  }
  sort(foo.begin(), foo.end(), cmp);
  
  for(int i = 0; i < foo.size(); i++)
  {
    if(curWeight + foo[i].second < capacity)
    {
      value = value + foo[i].first;
      curWeight = curWeight + foo[i].second;
    }
    else
    {
      int remain = capacity - curWeight;
      value = value + (foo[i].first)*((double)remain/foo[i].second);
      break;
    }
  }
  
  return value;
}

int main() {
  int n;
  int capacity;
  std::cin >> n >> capacity;
  vector<int> values(n);
  vector<int> weights(n);
  for (int i = 0; i < n; i++) {
    std::cin >> values[i] >> weights[i];
  }

  double optimal_value = get_optimal_value(capacity, weights, values);

  std::cout.precision(10);
  std::cout << optimal_value << std::endl;
  return 0;
}
