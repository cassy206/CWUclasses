#include <iostream>
#include <cstdlib>
#include <thread>
#include <unistd.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <sys/time.h>
#include <cstring>

using namespace std;

int main(int argc, char* argv[])
{
	int c;
	int sockfd = 0, n = 0;

	//default ip address
	char ip[256] = "127.0.0.1";
	const char* order = "Order started";

	//default port
	int port = 54321;

	//default max number of burgers
	int maxBurgers = 10;
	char buf[1024];
	struct sockaddr_in serv_addr;

	if (argc == 1) {
		cout << "Using IP Address --> 127.0.0.1" << endl;
		cout << "Using Port Number -- > 54321" << endl;
		cout << "Using default Max Burgers --> 10" << endl;
	}
	while ((c = getopt(argc, argv, "i:p:b:")) != -1)
	{
		switch (c)
		{
		case 'i':
			if (!strcpy(ip, optarg))
			{
				cout << "Using default ipAddress." << endl;
			}
			break;

		case 'p':
			n = atoi(optarg);
			if (n != 0)
			{
				port = n;
				cout << "Port number: " << port << endl;
				cout << "IP Address: " << ip << endl;
				cout << "Max number of burgers: " << maxBurgers << endl;
			}
			else
			{
				cout << "Port Invalid" << endl;
				cout << "Usage: ./client -i <IPAddress> -p <PortNumber>> -b <MaxNumberOfBUrgers>" << endl;
				exit(EXIT_FAILURE);
			}
			break;

		case 'b':
			n = atoi(optarg);
			if (n != 0)
			{
				maxBurgers = n;
				cout << "Max Number of burgers: " << maxBurgers << endl;
				cout << "Port number: " << port << endl;
				cout << "IP Address: " << ip << endl;
			}
			else
			{
				cout << "Incorrect number of burgers" << endl;
				cout << "Usage: ./client -i <IPAddress> -p <PortNumber>> -b <MaxNumberOfBUrgers>" << endl;
				exit(EXIT_FAILURE);
			}
			break;
		}
	}
	sockfd = socket(AF_INET, SOCK_STREAM, 0);
	if (sockfd < 0)
	{
		cout << "\n Error : Could not create socket \n";
		return 1;
	}

	cout << "\nSocket was created" << endl;

	serv_addr.sin_family = AF_INET;
	serv_addr.sin_port = htons(port);

	if (inet_pton(AF_INET, ip, &serv_addr.sin_addr) <= 0)
	{
		cout << "Incorrect IP address" << endl;
		cout << "Usage: ./client -i <IPAddress> -p <PortNumber>> -b <MaxNumberOfBUrgers> " << endl;
		exit(EXIT_FAILURE);
	}
	int attempts = 5;
	while (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0)
	{
		if (attempts == 0)
		{
			cout << "Attempting to connect again " << attempts << endl;
			attempts--;
			exit(EXIT_FAILURE);
		}
		cerr << "Could not connect to server." << endl;
		this_thread::sleep_for(chrono::seconds(1));
	}
	cout << "\nConnection has been established between client and server" << endl;

	cout << "\nSTART with " << maxBurgers << " burger orders" << endl;
	int burgerNumber = 1;  // Start with Burger #1
	while (maxBurgers > 0)
	{
		send(sockfd, order, strlen(order), 0);
		long resp = read(sockfd, buf, 1024);
		if (!resp)
		{
			cout << "No burger service." << endl;
			break;
		}

		srand(time(NULL));
		int randomNumber = rand() % 3;
		int waitTime = randomNumber ? randomNumber == 2 ? 7 : 5 : 3;
		this_thread::sleep_for(chrono::seconds(waitTime));

		// Print information about the consumed burger
		cout << "Burger #" << burgerNumber << ".\n";
		cout << "Eaten in " << waitTime << " seconds.\n";

		burgerNumber++;  // Increment after printing
		maxBurgers--;

		cout << "Orders remaining: " << maxBurgers << endl;
		if (maxBurgers == 0) {
			cout << "\nNo more Burger Orders." << endl;
			cout << "\nRun the program again to start Burger orders" << endl;
			cout << "Usage: ./client -i <IPAddress> -p <PortNumber> -b <MaxNumberOfBUrgers>" << endl;
		}
	}
	return 0;
}