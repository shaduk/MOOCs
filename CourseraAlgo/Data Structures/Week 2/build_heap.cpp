#include <iostream>
#include <vector>
#include <algorithm>

using std::vector;
using std::cin;
using std::cout;
using std::swap;
using std::pair;
using std::make_pair;
using namespace std;
class HeapBuilder {
 private:
  vector<int> data_;
  vector< pair<int, int> > swaps_;
    int size = 0;

  void WriteResponse() const {
    cout << swaps_.size() << "\n";
    for (int i = 0; i < swaps_.size(); ++i) {
      cout << swaps_[i].first << " " << swaps_[i].second << "\n";
    }
  }

  void ReadData() {
    int n;
    cin >> n;
    data_.resize(n);
    for(int i = 0; i < n; ++i)
      cin >> data_[i];
  }
    void swap(int i, int j)
    {
        swaps_.push_back(make_pair(j,i));
        int temp = data_[i];
        data_[i] = data_[j];
        data_[j] = temp;
     }
    
    void ShiftUp(int s)
    {
        if(data_[s] < data_[(s-1)/2])
        {
            swap(s,(s-1)/2);
            ShiftUp((s-1)/2);
        }
            
    }
    
    void ShiftDown(int s)
    {
        int lc = 2*s + 1, maxint = s;
        int rc = 2*s + 2;
        if(lc <= size && data_[maxint] > data_[lc])
            maxint = lc;
        if(rc <= size && data_[maxint] > data_[rc])
            maxint = rc;
        if(maxint != s)
        {
            swap(maxint, s);
            ShiftDown(maxint);
        }
    }
    
    void BuildHeap()
    {
        size = data_.size()-1;
        for(int i = data_.size()/2; i >= 0; i--)
        {
            ShiftDown(i);
        }
    }

  void GenerateSwaps() {
    swaps_.clear();
    // The following naive implementation just sorts 
    // the given sequence using selection sort algorithm
    // and saves the resulting sequence of swaps.
    // This turns the given array into a heap, 
    // but in the worst case gives a quadratic number of swaps.
    //
    // TODO: replace by a more efficient implementation
      BuildHeap();
  }

 public:
  void Solve() {
    ReadData();
    GenerateSwaps();
    WriteResponse();
  }

};

int main() {
  std::ios_base::sync_with_stdio(false);
  HeapBuilder heap_builder;
  heap_builder.Solve();
  return 0;
}
