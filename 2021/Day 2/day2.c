#include <stdlib.h>
#include <stdio.h>
#include <limits.h>

typedef struct {
	int x;
	int depth;
} SUBMARINE;

SUBMARINE* make_submarine() {
	SUBMARINE* sub = malloc(sizeof(SUBMARINE));
	sub->x = 0;
	sub->depth = 0;
	return sub;
}

int main(int argc, char **argv) {
	char *str;
	int mag;
	SUBMARINE *sub = make_submarine();
	FILE *input;
	input = fopen("input.txt", "r");
	printf("Opened file\n");
	while (fscanf(input, "%s %d\n", str, &mag) != EOF) {
		printf("%s\n", str);
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
}