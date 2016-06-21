#include <vector>
#include <utility>
#include <cmath>
#include "dtw.h"
#include <iostream>
#include <fstream>
#include <string>
#include <stdlib.h>

using namespace std;

vector<double> read_file(string filename);

namespace DTW {

    double dist(double x, double y) {
        return sqrt(pow((x - y), 2));
    }

    double dtw(const std::vector<double>& t1, const std::vector<double>& t2) {
        int m = t1.size();
        int n = t2.size();

        // create cost matrix
        double cost[m][n];

        cost[0][0] = dist(t1[0], t2[0]);

        // calculate first row
        for(int i = 1; i < m; i++)
            cost[i][0] = cost[i-1][0] + dist(t1[i], t2[0]);
        // calculate first column
        for(int j = 1; j < n; j++)
            cost[0][j] = cost[0][j-1] + dist(t1[0], t2[j]);
        // fill matrix
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
                cost[i][j] = std::min(cost[i-1][j], std::min(cost[i][j-1], cost[i-1][j-1])) 
                    + dist(t1[i],t2[j]);

        return cost[m-1][n-1];
    }
}



int main() {

   //  cout<< "dist_dtw=" << DTW::dtw(t1, t2) << endl;

    vector<double> acceleration = read_file("training.csv");

    vector<double> all_data[68];
    for (int i = 0;i<acceleration.size();i++)
    {
        int index = i/300;
        all_data[index].push_back(acceleration[i]);
    }
    
    vector<double> training[5];
    
    training[0] = all_data[1];
    training[1] = all_data[11];
    training[2] = all_data[32];
    training[3] = all_data[41];
    training[4] = all_data[57];
    
    cout << '[';
    for (int j = 0; j < 68;j++)
    {
        int min_dist = 100000;
        int min_index = -1;
        for (int k = 0; k < 5;k++)
        {
            double dist = DTW::dtw(all_data[j],training[k]);
            if (dist < min_dist)
            {
                min_dist = dist;
                min_index = k;
            }
        }
        cout << min_dist << ',';
    }
    cout << ']'<<endl;
    return 0;
}

vector<double> read_file(string filename)
{
    vector<double> acceleration;

    ifstream file("all.csv");
    string str; 
    while (getline(file, str))
    {

        int start_index = 0;
        int end_index = 0;
        for(int i = 0; i < str.size(); i++) 
        {  
            if (str[i] == ',')
            {
                int size = end_index-start_index;
                char data[size];
                for (int j =0; j < size; j++)
                {
                    data[j]=str[j+start_index];
                }   
                acceleration.push_back(atof(data));
                start_index = end_index+1;
            }
            end_index++;
        }
        int size = end_index-start_index;
        char data[size];
        for (int j =0; j < size; j++)
        {
            data[j]=str[j+start_index];
        }   
        acceleration.push_back(atof(data));
 


    }
  //  myfile.close();
    return acceleration;
}
