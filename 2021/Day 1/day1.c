#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

void part1() {
	int sonar;
	int prevSonar = INT_MAX;
	int numIncreased = 0;
	FILE *input;
	input = fopen("input.txt", "r");
	while (fscanf(input, "%d\n", &sonar) != EOF) {
		printf("%d\n", sonar);
		if (sonar > prevSonar) {
			numIncreased++;
		}
		prevSonar = sonar;
	}
	printf("Number of times sonar depth increased: %d\n", numIncreased);
	fclose(input);
}

int num_lines() {
	int sonar;
	int num_lines = 0;
	FILE *input;
	input = fopen("input.txt", "r");
	while (fscanf(input, "%d\n", &sonar) != EOF) {
		num_lines++;
	}
	fclose(input);
	return num_lines;
}

void part2() {
	FILE *input;
	input = fopen("input.txt", "r");
	int size = num_lines();
	int sonar, sonars[size];
	int line = 0;
	while (fscanf(input, "%d\n", &sonar) != EOF) {
		sonars[line] = sonar;
		line++;
	}
	fclose(input);
	
	int sum;
	int prevSum = INT_MAX;
	int numIncreased = 0;
	for (int i = 0; i < size - 2; i++) {
		sum = sonars[i] + sonars[i+1] + sonars[i+2];
		if (sum > prevSum) {
			numIncreased++;
		}
		prevSum = sum;
	}
	printf("Number of times sum increased: %d\n", numIncreased);
}

int main(int argc, char **argv) {
// 	part1();
	printf("num_lines: %d\n", num_lines());
	part2();
	return 0;
}