//==============================================================================
// Kdpartition
//
// @description: Program for printing out a set of (x,y) points in the order
//    they are visited during an in-order traversal of the kd-tree
// @author: Elisha Lai
// @version: 0.0.1 19/11/2015
//==============================================================================

// Kdpartition program (kdpartition.cpp)

#include <iostream>
#include <string>
#include <vector>
#include <utility>
#include <algorithm>

using namespace std;

// Stores the string representations of split directions
string splitDirections[] = {"Vertical", "Horizontal"};

// Returns the index of the selected pivot using the median
// of medians algorithm
int choosePivot(vector< pair<pair<int, int>, int> > &points) {
   if (points.size() <= 5) {
      return points[(points.size() / 2)].second;
   } else {
      const int m = ((points.size() / 5) - 1);

      // Creates a vector of medians from vectors of 5 points
      vector< pair< pair<int, int>, int> > medians;
      for (int i = 0; i <= m; i++) {
   	 // Creates a vector of 5 points
         vector< pair<pair<int, int>, int> > pointsGroup;
         for (int j = (5 * i); (j < ((5 * i) + 5)) && (j < points.size()); j++) {
            pointsGroup.push_back(points[j]);
         } // for
         
         // Stores the median of the vector of 5 points
         medians.push_back(pointsGroup[(pointsGroup.size() / 2)]);  
      } // for

      return medians[(medians.size() / 2)].second; 
   } // if
} // choosePivot

// Partitions a vector of points by their x-coordinates
int verticalPartition(vector< pair<int, int> > &points, int p) {
   swap(points[0], points[p]);
   int i = 0;
   int j = (points.size() - 1);

   while (true) {
      while ((i < points.size()) && (points[i].first <= points[0].first)) {
         i++;
      } // while
      
      while ((j >= 1) && (points[j].first > points[0].first)) {
         j--;
      } // while
   	  
      if (j < i) {
   	     break;
      } else {
         swap(points[i], points[j]);
      } // if
   } // while

   swap(points[0], points[j]);
   return j;
} // verticalPartition

// Partitions a vector of points by their y-coordinates
int horizontalPartition(vector< pair<int, int> > &points, int p) {
   swap(points[0], points[p]);
   int i = 0;
   int j = (points.size() - 1);

   while (true) {
      while ((i < points.size()) && (points[i].second <= points[0].second)) {
         i++;
      } // while
      
      while ((j >= 1) && (points[j].second > points[0].second)) {
         j--;
      } // while
   	  
      if (j < i) {
   	     break;
      } else {
         swap(points[i], points[j]);
      } // if
   } // while

   swap(points[0], points[j]);
   return j;
} // horizontalPartition

// Returns the point in position k of the sorted vector of points
// according to split direction 
pair<int, int> quickSelect(vector< pair<int, int> > &points,
	                         int k, string splitDirection) {
   // Creates a vector of points with their corresponding index
   vector< pair<pair<int, int>, int> > pointsWithIndex;
   for (int i = 0; i < points.size(); i++) {
      pointsWithIndex.push_back(make_pair(points[i],i));
   } // for

   const int p = choosePivot(pointsWithIndex);
   const int i = (splitDirection == "Vertical")?
      verticalPartition(points, p): horizontalPartition(points, p);

   if (i == k) {
      return points[i];
   } else if (i > k) {
      vector< pair<int, int> > leftPoints;
      for (int n = 0; n < i; n++) {
         leftPoints.push_back(points[n]);
      } // for
   	  
      return quickSelect(leftPoints, k, splitDirection);
   } else {
   	  vector< pair<int, int> > rightPoints;
   	  for (int n = (i + 1); n < points.size(); n++) {
   	  	 rightPoints.push_back(points[n]);
   	  } // for
   	  
   	  return quickSelect(rightPoints, (k - i - 1), splitDirection);
   } // if
} // quickSelect

// Prints out points in the order they are visited during an in-order
// traversal of the kd-tree
void kdPartition(vector< pair<int, int> > &points, int depth) {
   if (points.size() == 0) {
   	  return;
   } else {

      string splitDirection = splitDirections[(depth % 2)];
      pair<int, int> medianPoint = quickSelect(points, points.size() / 2, splitDirection);
      vector< pair<int, int> > leftSubtreePartition;
      vector< pair<int, int> > rightSubtreePartition;

      if (splitDirection == "Vertical") {
   	  
   	     // Partitions the points into the left and right subtree
   	     for (int i = 0; i < points.size(); i++) {
   	  	    if (points[i].first == medianPoint.first) {
   	  	 	     if (points[i].second == medianPoint.second) {
   	  	 	        continue;
   	  	 	     } else {
                  leftSubtreePartition.push_back(points[i]);
   	  	 	     } // if
   	  	    } else if (points[i].first < medianPoint.first) {
               leftSubtreePartition.push_back(points[i]);
   	  	    } else {
               rightSubtreePartition.push_back(points[i]);
   	  	    } // if
   	     } // for
   
      } else {
      
         // Partitions the points into the left and right subtree
         for (int i = 0; i < points.size(); i++) {
      	    if (points[i].second == medianPoint.second) {
      	 	     if (points[i].first == medianPoint.first) {
      	 	        continue;
      	 	     } else {
      	 	        leftSubtreePartition.push_back(points[i]);
      	 	     } // if
      	    } else if (points[i].second < medianPoint.second) {
      	 	     leftSubtreePartition.push_back(points[i]);
      	    } else {
      	 	     rightSubtreePartition.push_back(points[i]);
      	    } // if
         } // for
   
      } // if

      kdPartition(leftSubtreePartition, (depth + 1));
      cout << ' ' << medianPoint.first << ' ' << medianPoint.second;
      kdPartition(rightSubtreePartition, (depth + 1));
   } // if
} // kdPartition

int main() {
   int n = 0; // Stores the number of points
   cin >> n;

   // Reads in a vector of points
   vector< pair<int, int> > points;
   for (int i = 0; i < n; ++i) {
      int xCoord = 0;
      int yCoord = 0;
      cin >> xCoord >> yCoord;
      points.push_back(make_pair(xCoord, yCoord));
   } // for

   kdPartition(points, 0);
} // main
