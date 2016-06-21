/*
        demo-udp-03: udp-recv: a simple udp server
	receive udp messages

        usage:  udp-recv

        Paul Krzyzanowski
*/

#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <netdb.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include "port.h"
#include <iostream>
#include <stdlib.h>
#include <vector>
#include <utility>
#include <cmath>
#include <fstream>
#include "dtw.h"



using namespace std;


#define BUFSIZE 2048

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

vector<double> read_file(string filename);

int
main(int argc, char **argv)
{
	vector<double> acceleration = read_file("training.csv");

    vector<double> training[6];
    for (int i = 0;i<acceleration.size();i++)
    {
        int index = i/300;
        training[index].push_back(acceleration[i]);
    }
    
    // vector<double> training[5];
    
    // training[0] = all_data[1];
    // training[1] = all_data[11];
    // training[2] = all_data[32];
    // training[3] = all_data[41];
    // training[4] = all_data[57];

	struct sockaddr_in myaddr;	/* our address */
	struct sockaddr_in remaddr;	/* remote address */
	socklen_t addrlen = sizeof(remaddr);		/* length of addresses */
	int recvlen;			/* # bytes received */
	int fd;				/* our socket */
	unsigned char buf[BUFSIZE];	/* receive buffer */


	/* create a UDP socket */

	if ((fd = socket(AF_INET, SOCK_DGRAM, 0)) < 0) {
		perror("cannot create socket\n");
		return 0;
	}

	/* bind the socket to any valid IP address and a specific port */

	memset((char *)&myaddr, 0, sizeof(myaddr));
	myaddr.sin_family = AF_INET;
	myaddr.sin_addr.s_addr = htonl(INADDR_ANY);
	myaddr.sin_port = htons(SERVICE_PORT);

	if (bind(fd, (struct sockaddr *)&myaddr, sizeof(myaddr)) < 0) {
		perror("bind failed");
		return 0;
	}

	vector<double> signal(300, 0.0);
	//vector<double> a_y(100, 0.0);
	//vector<double> a_z(100, 0.0);

	/* now loop, receiving data and printing what we received */
	for (;;) {
		
		printf("waiting on port %d\n", SERVICE_PORT);
		recvlen = recvfrom(fd, buf, BUFSIZE, 0, (struct sockaddr *)&remaddr, &addrlen);
	//	printf("received %d bytes\n", recvlen);
		if (recvlen > 0) {
			buf[recvlen] = 0;
			//printf("received message: \"%s\"\n", buf);
	        int start_index = 0;
	        int end_index = 0;
	        int comma_count = 0; 
	        for(int i = 0; i < recvlen; i++) 
	        {  
	            if (buf[i] == ',')
	            {
	            	comma_count++;
	                int size = end_index-start_index;
	                char data[size];
	                if ((comma_count > 2) && (comma_count < 6))
	                {
	                	for (int j =0; j < size; j++)
	                	{
	                    	data[j]=buf[j+start_index];
	                	}
	                	if (comma_count == 3)
	                	{
							for (int x = 0;x<100;x++)
							{
								signal[x]=signal[x+1];
							
							}
							signal[99]=atof(data);
	                	}
	                	else if (comma_count == 4)
	                	{
							for (int x = 100;x<200;x++)
							{
								signal[x]=signal[x+1];
							}
							signal[199]=atof(data);
	                	}
	                	else
	                	{
							for (int x = 200;x<299;x++)
							{
								signal[x]=signal[x+1];
							}
							signal[299]=atof(data);
	                	}
	                }
	                start_index = end_index+1;
	            	
	            }
	            end_index++;
	        }

	    int min_dist = 100000;
        int min_index = -1;
        for (int k = 0; k < 5;k++)
        {
            double dist = DTW::dtw(signal,training[k]);
            if (dist < min_dist)
            {
                min_dist = dist;
                min_index = k;
            }
        }
        if (min_dist < 600)
        {
        	cout << min_index << endl;
        }


		}
	}
	/* never exits */
}


vector<double> read_file(string filename)
{
    vector<double> acceleration;

    ifstream file("training.csv");
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