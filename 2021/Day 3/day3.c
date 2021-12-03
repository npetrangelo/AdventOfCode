#include <stdlib.h>
#include <stdio.h>

int main(int argc, char **argv) {
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
		gamma |= (ones[i] > zeros[i]) << (11 - i);
		epsilon |=  (zeros[i] > ones[i]) << (11 - i);
	}
	printf("Power: %d\n", gamma * epsilon);
}