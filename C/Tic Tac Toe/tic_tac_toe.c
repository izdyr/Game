#include <stdio.h>
#include <stdbool.h>

#define BOARD_SIZE 3

void draw_board(char board[BOARD_SIZE][BOARD_SIZE]) {
    int i, j;
    for (i = 0; i < BOARD_SIZE; i++) {
        for (j = 0; j < BOARD_SIZE; j++) {
            printf(" %c ", board[i][j]);
            if (j < BOARD_SIZE - 1) {
                printf("|");
            }
        }
        printf("\n");
        if (i < BOARD_SIZE - 1) {
            printf("---+---+---\n");
        }
    }
}

bool check_win(char board[BOARD_SIZE][BOARD_SIZE], char symbol) {
    int i, j;

    for (i = 0; i < BOARD_SIZE; i++) {
        bool win = true;
        for (j = 0; j < BOARD_SIZE; j++) {
            if (board[i][j] != symbol) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }

    for (i = 0; i < BOARD_SIZE; i++) {
        bool win = true;
        for (j = 0; j < BOARD_SIZE; j++) {
            if (board[j][i] != symbol) {
                win = false;
                break;
            }
        }
        if (win) {
            return true;
        }
    }

    bool diagonal1_win = true;
    bool diagonal2_win = true;
    for (i = 0; i < BOARD_SIZE; i++) {
        if (board[i][i] != symbol) {
            diagonal1_win = false;
        }
        if (board[i][BOARD_SIZE - 1 - i] != symbol) {
            diagonal2_win = false;
        }
    }
    if (diagonal1_win || diagonal2_win) {
        return true;
    }

    return false;
}

int main() {
    char board[BOARD_SIZE][BOARD_SIZE];
    int i, j, num_turns = 0;
    bool game_over = false;

    for (i = 0; i < BOARD_SIZE; i++) {
        for (j = 0; j < BOARD_SIZE; j++) {
            board[i][j] = ' ';
        }
    }

    while (!game_over && num_turns < BOARD_SIZE * BOARD_SIZE) {
        draw_board(board);

        int row, col;
        char symbol;
        if (num_turns % 2 == 0) {
            printf("Player X's turn: ");
            symbol = 'X';
        } else {
            printf("Player O's turn: ");
            symbol = 'O';
        }
        scanf("%d %d", &row, &col);

        if (row < 1 || row > BOARD_SIZE || col < 1 || col > BOARD_SIZE || board[row - 1][col - 1] != ' ') {
            printf("Invalid move!\n");
            continue;
        }

        board[row - 1][col - 1] = symbol;
        num_turns++;

        if (check_win(board, symbol)) {
            game_over = true;
            printf("Player %c wins!\n", symbol);
        }
    }

    if (!game_over) {
        printf("Game over: tie!\n");
    }

    draw_board(board);

    return 0;
}
