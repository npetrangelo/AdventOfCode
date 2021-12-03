#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

typedef struct {
	int x;
	int depth;
	int aim;
} SUBMARINE;

SUBMARINE* make_submarine() {
	SUBMARINE* sub = malloc(sizeof(SUBMARINE));
	sub->x = 0;
	sub->depth = 0;
	sub->aim = 0;
	return sub;
}

void part1() {
	char str[10];
	int mag;
	SUBMARINE *sub = make_submarine();
	FILE *input;
	input = fopen("input.txt", "r");
	printf("Opened file\n");
	while (fscanf(input, "%s %d\n", str, &mag) != EOF) {
		switch (str[0]) {
			case 'f':
				sub->x += mag;
				break;
			case 'u':
				sub->depth -= mag;
				break;
			case 'd':
				sub->depth += mag;
				break;
		}
	}
	printf("Product of final x and depth: %d\n", sub->x * sub->depth);
	free(sub);
}

void part2() {
	char str[10];
	int mag;
	SUBMARINE *sub = make_submarine();
	FILE *input;
	input = fopen("input.txt", "r");
	printf("Opened file\n");
	while (fscanf(input, "%s %d\n", str, &mag) != EOF) {
		switch (str[0]) {
			case 'f':
				sub->x += mag;
				sub->depth += mag * sub->aim;
				break;
			case 'u':
				sub->aim -= mag;
				break;
			case 'd':
				sub->aim += mag;
				break;
		}
	}
	printf("Product of final x and depth: %d\n", sub->x * sub->depth);
	free(sub);
}

int main(int argc, char **argv) {
// 	part1();
	part2();
	return 0;
}