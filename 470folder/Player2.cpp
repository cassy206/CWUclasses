#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/shm.h>
#include <string.h>
#include <iostream>
#include <vector>
#include <string>
#include <cstdlib>

#define MAX_SIZE 10

//function to print the game board
void print_grid(char* grid, int size) {
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            printf("%c ", grid[i * size + j]);
        }
        printf("\n");
    }
    printf("\n");
}

int check_win(char* grid, int size, char symbol) {
    // Check rows
    for (int i = 0; i < size; i++) {
        int win = 1;
        for (int j = 0; j < size; j++) {
            if (grid[i * size + j] != symbol) {
                win = 0;
                break;
            }
        }
        if (win) return 1;
    }

    // Check columns
    for (int i = 0; i < size; i++) {
        int win = 1;
        for (int j = 0; j < size; j++) {
            if (grid[j * size + i] != symbol) {
                win = 0;
                break;
            }
        }
        if (win) return 1;
    }

    // Check diagonal
    int win = 1;
    for (int i = 0; i < size; i++) {
        if (grid[i * size + i] != symbol) {
            win = 0;
            break;
        }
    }
    if (win) return 1;

    // Check anti-diagonal
    win = 1;
    for (int i = 0; i < size; i++) {
        if (grid[i * size + (size - i - 1)] != symbol) {
            win = 0;
            break;
        }
    }
    if (win) return 1;

    return 0;
}

int main(int argc, char** argv) {
    if (argc == 1) {
        printf("Usage: %s size not given. Enter GridSize between 3 and 9 when compiling file\n", argv[0]);
        return 1;
    }

    int size = atoi(argv[1]);

    if (size < 3 || size > MAX_SIZE) {
        printf("Invalid size. Grid size must be between 3 and 9\n");
        return 1;
    }

    int shmid;
    char* grid;

    // Access shared memory
    key_t key = ftok("player1.cpp", 'R');
    shmid = shmget(key, size * size, 0666);

    if (shmid < 0) {
        perror("shmget");
        return 1;
    }

    // Attach shared memory
    grid = (char*)shmat(shmid, NULL, 0);

    if (grid == (char*)-1) {
        perror("shmat");
        return 1;
    }

    // Play the game
    char symbol = 'O';
    int num_turns = 1;

    while (num_turns < size * size) {
        // Read player input
        int row, col;
        int valid_input = 0;
        while (!valid_input) {
            char input[10]; // Assuming the input won't be longer than 10 characters
            printf("Player (%c), enter row and column (or type 'exit' to quit): ", symbol);
            fgets(input, sizeof(input), stdin);
            input[strcspn(input, "\n")] = '\0';

            if (strcmp(input, "exit") == 0) {
                printf("Player (%c) has exited the game.\n", symbol);
                return 0; // Exit the game
            }

            if (sscanf(input, "%d %d", &row, &col) == 2 && row >= 1 && row <= size && col >= 1 && col <= size) {
                if (grid[(row - 1) * size + (col - 1)] == '-') {
                    valid_input = 1;
                }
                else {
                    printf("Invalid move. The space is already taken.\n");
                }
            }
            else {
                printf("Invalid input. Enter 'row col' or 'exit' to quit.\n");
            }
        }
        // Make a move
        grid[(row - 1) * size + (col - 1)] = symbol;

        // Print updated grid
        print_grid(grid, size);

        // Check for win or draw
        if (check_win(grid, size, symbol)) {
            printf("Player (%c) wins!\n", symbol);
            break;
        }
        else if (num_turns == size * size - 1) {
            printf("It's a draw!\n");
            break;
        }

        // Switch players
        symbol = (symbol == 'X') ? 'O' : 'X';
        num_turns++;
    }

    // Detach shared memory
    if (shmdt(grid) == -1) {
        perror("shmdt");
        return 1;
    }

    return 0;
}