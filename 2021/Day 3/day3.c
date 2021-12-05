#include <stdlib.h>
#include <stdio.h>
#include <string.h>

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

int calculate_oxygen() {
    char oxygen[13] = "";
    char str[13];
    int zeros[12] = {0};
    int ones[12] = {0};
    FILE *input;

    char format[15] = "";
    int numMatches;
    printf("Begin loop\n");
    for (int i = 0; i < 12; i++) {
        printf("i = %d\n", i);
        strcpy(format, oxygen);
        strcat(format, "%s\n");
        printf("Opening file, format = %s\n", format);
        input = fopen("input.txt", "r");
        while ((numMatches = fscanf(input, format, str)) != EOF) {
            if (numMatches == 0) {
                fscanf(input, "%*s\n");
                continue;
            }
            printf("i=%d, numMatches=%d, str=%s\n", i, numMatches, str);
            switch (str[i]) {
                case '0':
                    zeros[i]++;
                    break;
                case '1':
                    ones[i]++;
                    break;
            }
            printf("End while loop\n");
        }
        printf("Closing file\n");
        fclose(input);
        char new = (ones[i] >= zeros[i]) + '0';
        printf("new = %c\n", new);
        strncat(oxygen, &new, 1);
        printf("oxygen rate = %s\n", oxygen);
    }

    int oxygen_rate = 0;
    for (int i = 0; i < 12; i++) {
        oxygen_rate <<= 1;
        oxygen_rate |= oxygen[i] - '0';
    }

    return oxygen_rate;
}

void part2() {
    printf("Oxygen: %d\n", calculate_oxygen());
}

void foo() {
    char str[13];
    FILE *input;
    input = fopen("input.txt", "r");
    fscanf(input, "000001000%s", str);
    printf("%s\n", str);
}

int main(int argc, char **argv) {
    part2();
}
