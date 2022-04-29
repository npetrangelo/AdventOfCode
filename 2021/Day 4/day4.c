#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* filename = "test.txt";

typedef struct {
    int size;
    int (*arr)[];
} LIST;

LIST* make_list() {
    l->size = 0;
    LIST* l = malloc(sizeof(LIST));
}

void free_list(LIST *l) {
    free(l->arr);
    free(l);
}

int fill_bingo_board(FILE *input, int board[5][5]) {
    puts("Printing Bingo Board");
    int numMatches;
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            numMatches = fscanf(input, "%d", &board[i][j]);
            if (numMatches == EOF) {
                return EOF;
            }
        }
    }
    return 1;
}

void print_board(int board[5][5]) {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            printf("%d ", board[i][j]);
        }
        printf("\n");
    }
}

void part1() {
    int numDraws = 0;
    int draws[100];
    int draw;
    puts("Opening file");
    FILE *input;
    input = fopen(filename, "r");
    int numMatches = 0;
    fscanf(input, "%d", &draw);
    draws[numDraws++] = draw;
    while ((numMatches = fscanf(input, ",%d", &draw)) > 0) {
//         printf("numMatches=%d match=%d\n", numMatches, draw);
        draws[numDraws++] = draw;
    }

    for (int i = 0; i < numDraws; i++) {
        printf("%d,", draws[i]);
    }
    printf("\n");

    int board1[5][5];
    fill_bingo_board(input, board1);
    print_board(board1);
}

int main(int argc, char **argv) {
    part1();
}
