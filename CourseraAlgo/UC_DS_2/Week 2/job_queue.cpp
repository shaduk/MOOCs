#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <stack>

using std::vector;
using std::cin;
using std::cout;
using namespace std;

class JobQueue {
 private:
  int num_workers_;
  vector<int> jobs_;
  
  vector<int> assigned_workers_;
  vector<long long> start_times_;
  vector<int> thread;
  std::stack<int> jobs;
  priority_queue<int> threadpq;
  
  void WriteResponse() const {
    for (int i = 0; i < assigned_workers_.size(); ++i) {
      cout << assigned_workers_[i] << " " <<  start_times_[i] << "\n";
    }
  } 

  void ReadData() {
    int m;
    cin >> num_workers_ >> m;
    jobs_.resize(m);
    thread.resize(num_workers_);
    for(int i = 0; i < m; ++i)
    {
      cin >> jobs_[i];
      jobs.push(jobs_[i]);
    }
    for(int i = 0; i < num_workers_; i++)
      thread[i] = 0;
    for(int j = 0; j < thread.size(); j++)
          {
            threadpq.push(j);
          }
  }

  void AssignJobs() {
    // TODO: replace this code with a faster algorithm.
    assigned_workers_.resize(jobs_.size());
    start_times_.resize(jobs_.size());
     int next_worker;
     int job;
      while(!jobs.empty())
      {
        while(!threadpq.empty() && !jobs.empty())
          {
             job = jobs.top();
             jobs.pop();
             next_worker = threadpq.top();
             threadpq.pop();
             thread[next_worker] = job;
             assigned_workers_.push_back(next_worker);
          }
          for(int i = 0; i < thread.size(); i++)
          {
            thread[i] = thread[i] - 1;
            if(thread[i] == 0)
              threadpq.push(i);
          }
      }
      
  }

 public:
  void Solve() {
    ReadData();
   AssignJobs();
   WriteResponse();
  }
};

int main() {
  std::ios_base::sync_with_stdio(false);
  JobQueue job_queue;
  job_queue.Solve();
  return 0;
}
