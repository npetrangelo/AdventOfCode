#include <stdlib.h>
#include <stdio.h>
#include <string.h>

char* filename = "input.txt";

// Assumes little endian
void printBits(size_t const size, void const * const ptr)
{
    unsigned char *b = (unsigned char*) ptr;
    unsigned char byte;
    int i, j;

    for (i = size-1; i >= 0; i--) {
        for (j = 7; j >= 0; j--) {
            byte = (b[i] >> j) & 1;
            printf("%u", byte);
        }
    }
}

void part1() {
    char str[13];
    int zeros[12] = {0};
    int ones[12] = {0};
    FILE *input;
    input = fopen("input.txt", "r");
    printf("Opened file\n");
    while (fscanf(input, "%s\n", str) != EOF) {
        for (int i = 0; i < 12; i++) {
            switch (str[i]) {
                case '0':
                    zeros[i]++;
                    break;
                case '1':
                    ones[i]++;
                    break;
            }
        }
    }
    fclose(input);

    int gamma = 0;
    int epsilon = 0;
    for (int i = 0; i < 12; i++) {
        gamma <<= 1;
        epsilon <<= 1;
        gamma |= (ones[i] > zeros[i]);
        epsilon |=  (zeros[i] > ones[i]);
    }
    printf("Power: %d\n", gamma * epsilon);
}

int num_lines() {
	int num_lines = 0;
	FILE *input;
	input = fopen(filename, "r");
	while (fscanf(input, "%*d\n") != EOF) {
		num_lines++;
	}
	fclose(input);
	return num_lines;
}

void fill_numbers(int numbers[]) {
    char str[13];
    FILE *input;
    input = fopen(filename, "r");
    int line = 0;
    while (fscanf(input, "%s\n", str) != EOF) {
        numbers[line] = strtol(str, NULL, 2);
        line++;
    }
}

int most_frequent(int arr[], int size, int position) {
    int balance = 0;
    for (int i = 0; i < size; i++) {
        if ((arr[i] >> position) & 0b1) {
            balance++;
        } else {
            balance--;
        }
    }
    return balance >= 0;
}

int least_frequent(int arr[], int size, int position) {
    int balance = 0;
    for (int i = 0; i < size; i++) {
        if ((arr[i] >> position) & 0b1) {
            balance++;
        } else {
            balance--;
        }
    }
    return balance < 0;
}

int step(int old[], int new[], int size, int position, int match) {
    printf("Match = %d at position = %d\n", match, position);
    int j = 0;
    printf("[");
    for (int i = 0; i < size; i++) {
        if (((old[i] >> position) & 0b1) == match) {
//             printf("Adding to list 0x%x\n", old[i]);
            printBits(2, &old[i]);
            printf(", ");
            new[j++] = old[i];
        }
    }
    printf("]\n");
    return j;
}

int calc_oxygen(int numbers[], int size) {
    puts("Calculating oxygen");
    int aNumbers[size];
    int bNumbers[size];

    memset(aNumbers, 0, sizeof(aNumbers[0]));
    memset(bNumbers, 0, sizeof(bNumbers[0]));

    size = step(numbers, aNumbers, size, 11, most_frequent(numbers, size, 11));
    for (int i = 10; i > 1; i -= 2) {
        if (size == 1) {
            return aNumbers[0];
        }
        printf("asize=%d\n", size);
        size = step(aNumbers, bNumbers, size, i, most_frequent(aNumbers, size, i));
        if (size == 1) {
            return aNumbers[0];
        }
        printf("bsize=%d\n", size);
        size = step(bNumbers, aNumbers, size, i-1, most_frequent(bNumbers, size, i-1));
    }
    printf("asize=%d\n", size);
    size = step(aNumbers, bNumbers, size, 0, most_frequent(bNumbers, size, 0));
    return bNumbers[0];
}

int calc_carbon(int numbers[], int size) {
    puts("Calculating carbon");
    int aNumbers[size];
    int bNumbers[size];

    memset(aNumbers, 0, sizeof(aNumbers[0]));
    memset(bNumbers, 0, sizeof(bNumbers[0]));

    size = step(numbers, aNumbers, size, 11, least_frequent(numbers, size, 11));
    for (int i = 10; i > 1; i -= 2) {
        if (size == 1) {
            return aNumbers[0];
        }
        printf("asize=%d\n", size);
        size = step(aNumbers, bNumbers, size, i, least_frequent(aNumbers, size, i));
        if (size == 1) {
            return aNumbers[0];
        }
        printf("bsize=%d\n", size);
        size = step(bNumbers, aNumbers, size, i-1, least_frequent(bNumbers, size, i-1));
    }
    printf("asize=%d\n", size);
    size = step(aNumbers, bNumbers, size, 0, most_frequent(bNumbers, size, 0));
    return bNumbers[0];
}

void part2() {
    int size = num_lines();
    int input[size];
    fill_numbers(input);
    int oxygen = calc_oxygen(input, size);
    int carbon = calc_carbon(input, size);
    printf("Oxygen = %d, Carbon = %d, Product = %d\n", oxygen, carbon, oxygen*carbon);
}

int main(int argc, char **argv) {
    part2();
}
