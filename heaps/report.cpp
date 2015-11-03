//==============================================================================
// Report
//
// @description: Program for printing out the integers in a heap greater than
//    or equal to an integer
// @author: Elisha Lai
// @version: 0.0.1 02/11/2015
//==============================================================================

// Report program (report.cpp)

#include <iostream>
#include <vector>

using namespace std;

// Prints out the elements in v that are greater than or equal to c.
void greaterThanOrEqual(vector<int> &v, int n, int c, int i) {
   const int leftChildPos = ((2 * i) + 1);
   const int rightChildPos = ((2 * i) + 2);

   if (i >= n) {          // Index out of bounds?
      return;
   } else if (v[i] < c) { // Element less than c?
      return;
   } else {
      cout << v[i] << endl;
      greaterThanOrEqual(v, n, c, leftChildPos);
      greaterThanOrEqual(v, n, c, rightChildPos);
   } // if
} // report

int main() {
   int n = 0; // Stores the number of elements in array
   cin >> n;

   // Reads in an array of integers
   vector<int> v;
   for (int i = 0; i < n; ++i) {
      int num = 0;
      cin >> num;
      v.push_back(num);
   } // for

   int c = 0;
   cin >> c;

   greaterThanOrEqual(v, n, c, 0);  
} // main
