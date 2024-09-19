// Lab2.cpp : This file contains the 'main' function. Program execution begins and ends there.
//
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

using namespace std;

//function to print the game board
void print_board(vector<vector<string>> board, int row, int col)
{
    for (int i = 0; i < row; i++)
    { 
        for (int j = 0; j < col; j++)
        {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Functions to check if a player has won
//row win
bool rowWin(vector<vector<string>>& board, const string& playerID)
{
    bool win = true;
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board.size(); j++){
            if (board[j][i] != playerID) {
               win = false;
            }
        }
        if (win) {
            return true;
        }
        else {
            win = true;
        }
    }
    return false;
}
//column win

bool colWin(vector<vector<string>>& board, const string& playerID) {
    
    bool win = true;

    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board.size(); j++) {
            if (board[i][j] != playerID) {
                win = false;
            }
        }
        if (win){
            return true;
        }
        else {
            win = true;
        }
    }
    return false;
}
    // Check for diagonal win
bool crossWin(vector<vector<string>>& board, const string& playerID) {
   
    bool win = true;
    for (int i = 0; i < board.size(); i++) {
        if (board[i][i] != playerID) {
            win = false;
        }
    }
    if (win) {
        return true;
    }
    else {
        win = true;
    }

    for (int i = board.size() - 1; i > -1; i--) {
        if (board[board.size() - i - 1][i] != playerID) {
            win = false;
        }
    }
    if (win) {
        return true;
    }
    else {
        win = true;
    }
    return false;
}

//Function to handle invalid inputs for player moves
bool invalidMove(vector<vector<string>>& board, int x, int y)
{
    if (x < 0 || y < 0 || x >= board.size() || y >= board.size())
    {
        cout << "Invalid move. Coordinates not found \n" << endl;
        cout << "Please enter two numbers for x and y coordinates within given grid. \n" << endl;
        cout << "Rows and Columns start at 0 not 1 so if you have a 3 x 3 board the biggest number for row or column is 2 \n" << endl;
        return true;
    }
    if (board[x][y] != "|")
    {
        cout << "Invalid move. The space is already taken." << endl;
        cout << "Please enter two numbers for x and y coordinates within given grid." << endl;
        return true;
    }
    return false;
}

bool win(vector<vector<string>>& board, const string& playerID)
{
    if (rowWin(board, playerID) || colWin(board, playerID) || crossWin(board, playerID)) {
        if (playerID == "X") {
            cout << "Player 1 wins!\n" << endl;
        }
        else {
            cout << "Player 2 wins!\n" << endl;
        }
        return true;
    }
    return false;
}
int main(int argc, char* argv[]) {
    int row = 0, col = 0;

    //Error checking the command line arguments for no parameters and limiting grids to equal numbers above 3
    if (argc == 1)
    {   
        cout << "Please enter two equal numbers greater than 2 for the grid size" << endl;
        // Prompt the user to enter the board size
        while (row < 2  || col < 2 || row != col) {
            cout << "Enter the board size (i.e. 3 3 or 9 9): ";
            cin >> row >> col;
            if (row < 2 || col < 2 || row != col) {
                cout << "Invalid board size, please enter two equal numbers greater than 2." << endl;
            }
        }
    }
    else if (argc != 3 || atoi(argv[1]) < 3 || atoi(argv[2]) < 3 || atoi(argv[1]) != atoi(argv[2]))
    {
        cout << "Invalid input for board size entered." << endl;
        cout << "Please enter two equal numbers greater than 2 for the board size i.e. 3 3 or 9 9" << endl;
        // Prompt the user to enter the board size
        while (row < 2 || col < 2 || row != col) {
            cout << "Enter the board size i.e. 3 3 or 4 4 ";
            cin >> row >> col;
            if (row < 2 || col < 2 || row != col) {
                cout << "Invalid board size, please enter two equal numbers greater than 2." << endl;
            }
        }
    }
    else {
        row = atoi(argv[1]);
        col = atoi(argv[2]);
    }
    vector<vector<string>> board(row, vector<string>(col, "|"));

    print_board(board, row, col);

    //Creating players and running game
    string playerID = "X";
    int counter = 0;

    do
    {
        int x;
        int y;
        cout << playerID << "'s turn. Please enter in a valid coordinate to place your symbol: ";
        cin >> x >> y;

        //Checking for invalid moves from player input
        if (invalidMove(board, x, y)) {
            continue;
        }

        //updating board with correct player input
        counter++;
        board[x][y] = playerID;

        //Checking for win conditions
        if (win(board, playerID))
        {
            break;
        }

        //Changing to next player
        playerID = (playerID == "X") ? "O" : "X";

        //Printing updated board
        print_board(board, row, col);

        //Checking for draw
        if (counter == (x * y))
        {
            cout << "Draw!" << endl;
            break;
        }
    } while (true);

    //Printing final board after win or draw and clearing memory
   print_board(board, row, col);
    board.clear();
    return 0;
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
