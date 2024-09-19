// LInuxLab.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <cstdlib>
#include <stdlib.h>
#include <cstdio>
#include <sys/types.h>
#include <sys/stat.h>
#include <array>
#include <memory>
#include <stdexcept>
#include <fstream>
#include <filesystem>
#include <string>
#include <sys/utsname.h>


using namespace std;

#define MAX_COMMAND_LEN 120
#define MAX_ARGS_LEN 120

int data_token_len = 0;
string shell_prompt = "cwushell>";
bool loop_shell = true;
int exit_code = 0;

enum Commands {
	exit_command,
	prompt,
	fileinfo,
	osinfo,
	system_command,
	manual_command_enum,
};

Commands convert_commands(string cmd)
{
	if (cmd == "exit") return Commands::exit_command;
	else if (cmd == "prompt") return Commands::prompt;
	else if (cmd == "fileinfo") return Commands::fileinfo;
	else if (cmd == "osinfo") return Commands::osinfo;
	else if (cmd == "manual") return Commands::manual_command_enum;
	else return Commands::system_command;
}

string* split(string str, char del, string* result)
{
	string temp = "";
	int pos = 0;
	for (int i = 0; i < str.size(); i++)
	{
		if (str[i] == del & temp != "")
		{
			result[pos] = temp;
			temp = "";
			pos++;
		}
		else
		{
			temp += str[i];
		}
	}
	if (temp != "")
	{
		result[pos] = temp;
		pos++;
	}

	data_token_len = pos;
	return result;
}
void cwushell_startup()
{
	system("clear");
}


void exit_shell(string* data)
{

	cout << exit_code << endl;
	std::exit(exit_code);
}

//prompt [new_prompt]
int change_prompt(string* data) {
	string new_prompt = "cwushell>";
	if (data_token_len == 1)
	{
		shell_prompt = new_prompt;
		return 1;
	}
	if (data_token_len == 2)
	{
		new_prompt = data[1];
		shell_prompt = new_prompt;
		return 1;
	}
	else
	{
		cout << "Too many prompts, prompt left unchanged.";
		return 1; // unrecognized 

	}
}

//manual command 
void manual_command(const string& cmd) {
	if (cmd == "manual") {
		cout << "Commands, Syntax and outcomes of different prompts in the shell" << endl;
		cout << "cd command allows the user to change the current working directory" << endl;
		cout << "pwd prints the current working directory" << endl;
		cout << "history prints the command history" << endl;
		cout << "prompt allows the user to change the prompt message." << endl;
		cout << "fileinfo [-i | -t| -m] <filename> allows a user to view different file related information based on the switch." << endl;
		cout << "osinfo [-S | -v | -a] -- will print on the screen different system-related information based on the switch." << endl;
	}
	else {
		cout << "Command not found: " << cmd << endl;
	}
}
// returns a boolean array corresponding to the string of switches provided

bool* get_switches(string* data, string switches_full, bool* active_switches)
{
	int active_switches_size = switches_full.size() + 1;
	string switches = "";
	for (int i = 1; i < data_token_len; i++)
	{
		if (data[i][0] == '-')
		{
			for (int j = 1; j < data[i].size(); j++)
			{
				switches += data[i][j];
			}
			//cout<< data[i] << endl;
		}
	}
	// convert the switches provided to a boolean array
	for (int i = 0; i < switches.size(); i++)
	{
		char sw = switches[i];
		//cout << sw << " switch processing" << endl; 
		bool sw_used = false;
		for (int j = 0; j < switches_full.size(); j++)
		{
			if (sw == switches_full[j])
			{
				//cout << "using switch " << endl;
				active_switches[j] = true;
				sw_used = true;
			}

		}
		//improper switch used
		if (!sw_used)
		{
			cout << "Switch not recognized " << sw << "" << endl;
			active_switches[active_switches_size - 1] = true;
		}
	}

	return active_switches;
}
int fileinfo_command_exec(bool* switches, string filename)
{
	//-i from stat filename -c %i "inode"
	//-t from stat filename -c %F
	//-m from stat filename -c %y "

	if (switches[3])
	{
		cout << "improper switch usage" << endl;
		return 1;
	}
	if (switches[0])
	{
		/*string inode_querry = (" echo Inode Number:  `stat "+filename + " -c %i`");
		(system(inode_querry.c_str()));*/
		int inode;
		struct stat file_stat;
		int ret;
		ret = stat(filename.c_str(), &file_stat);

		inode = file_stat.st_ino;
		cout << "Inode Number: " << inode << endl;
	}
	if (switches[1])
	{
		string filetype_querry = ("echo File type: `stat " + filename + " -c %F`");
		system(filetype_querry.c_str());
	}
	if (switches[2])
	{

		struct stat file_stat;
		int ret;
		ret = stat(filename.c_str(), &file_stat);
		cout << "Last: " << file_stat.st_mtime << endl;
	}
	return 0;
}
//fileinfo -i -t -m  filename 
//	(default is -itm or inode, type, modified date)
int fileinfo_command(string* data)
{
	string filename;
	bool cmd_switches[4] = { 0 };
	get_switches(data, "itm", cmd_switches);
	for (int i = 1; i < data_token_len; i++)
	{
		if (data[i][0] != '-')
		{
			if (filename.empty())
			{
				filename = data[i];
			}
			else
			{
				cout << "Too many file names provided. " + data[i] << endl;
				return 1; // bad exit code
			}
		}
	}
	fstream file_stream;
	file_stream.open(filename);
	if (file_stream.fail())
	{
		file_stream.close();
		cout << "File does not exist." << endl;;
		return 1;
	}
	return fileinfo_command_exec(cmd_switches, filename);
}
//osinfo -Sprint the operating system running on the machine,v –will print the version of the OS and 3) - a – will print the computer architecture
int osinfo_command(string* data)
{
	bool switches[3] = { 0 };
	// Function to check for switches and set corresponding flags
	get_switches(data, "Sva", switches);

	for (int i = 1; i < data_token_len; i++)
	{
		if (data[i][0] != '-')
		{
			cout << "unexpected token " + data[i] << endl;
			return 2;
		}
	}

	if (!(switches[0] || switches[1] || switches[2]))
	{
		cout << "No valid switch provided" << endl;
		return 1;
	}

	// -S switch: Print the operating system name
	if (switches[0])
	{
		struct utsname os_info;
		if (uname(&os_info) == 0)
		{
			cout << "Operating System: " << os_info.sysname << endl;
		}
		else
		{
			cout << "Failed to retrieve operating system information" << endl;
		}
	}

	// -v switch: Print the version of the operating system
	if (switches[1])
	{
		struct utsname os_info;
		if (uname(&os_info) == 0)
		{
			cout << "OS Version: " << os_info.version << endl;
		}
		else
		{
			cout << "Failed to retrieve operating system information" << endl;
		}
	}

	// -a switch: Print the computer architecture (32-bit or 64-bit)
	if (switches[2])
	{
		struct utsname os_info;
		if (uname(&os_info) == 0)
		{
			cout << "Computer Architecture: " << os_info.machine << endl;
		}
		else
		{
			cout << "Failed to retrieve operating system information" << endl;
		}
	}

	return 0;
}
//all other shell commands
int shell_command(string cmd)
{
	const char* command = cmd.c_str();
	return system(command);
}

//		handler for switching between commands, then switching between switches
// 			formatting parameters

int command_switch(string* data, string raw_input)
{
	if (data_token_len == 0)
	{
		return 0;
	}
	string cmd = data[0];
	Commands command = convert_commands(cmd);
	switch (command)
	{
	case Commands::exit_command:
		exit_shell(data);
		break;
	case Commands::prompt:
		return change_prompt(data);
		break;
	case Commands::fileinfo:
		return fileinfo_command(data);
		break;
	case Commands::osinfo:
		return osinfo_command(data);
		break;
	case Commands::system_command:
		return shell_command(raw_input);
		break;
	case Commands::manual_command_enum:
		// Assuming "manual" is the keyword
		if (data[0] == "manual") {
			manual_command(data[0]); // Pass the command as a parameter
		}
		else {
			return shell_command(raw_input);
		}
		break;
	}
	return 0;
}
//		buffer



int main(int argc, char* argv[])
{
	//startup
	cwushell_startup();
	char delimeter = ' ';
	while (true)
	{
		//loop
		cout << shell_prompt;
		char input[MAX_COMMAND_LEN];
		cin.getline(input, MAX_COMMAND_LEN);
		string result[MAX_ARGS_LEN];

		string* data = split(input, delimeter, result);
		exit_code = command_switch(data, input);
	}
	//exit

	return EXIT_SUCCESS;
}


// Run program: Ctrl + F5 or Debug > Start Without Debugging menu
// Debug program: F5 or Debug > Start Debugging menu

// Tips for Getting Started: 
//   1. Use the Solution Explorer window to add/manage files
//   2. Use the Team Explorer window to connect to source control
//   3. Use the Output window to see build output and other messages
//   4. Use the Error List window to view errors
//   5. Go to Project > Add New Item to create new code files, or Project > Add Existing Item to add existing code files to the project
//   6. In the future, to open this project again, go to File > Open > Project and select the .sln file
