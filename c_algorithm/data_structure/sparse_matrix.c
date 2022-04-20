#include <stdio.h>
#include <assert.h>
#include "smatrix.h"

//time complexity : O(n^2)

void smadd(matrix a, matrix b, matrix d) {
	assert((a != NULL) && (b != NULL) && (d != NULL));
	assert((a[0].row == b[0].row) && (a[0].col == b[0].col));
	assert(a[0].col > 0);
	int i = 1, j = 1, k = 1;
	d[0].row = a[0].row;
	d[0].col = a[0].col;

	while (i <= a[0].value || j <= b[0].value) {
		//fill in matrix D by comparing row and columns
		if (a[i].row == b[j].row) {
			if (a[i].col == b[j].col) {
				d[k].row = a[i].row;
				d[k].col = a[i].col;
				d[k++].value = a[i++].value + b[j++].value;
			}
			else if (a[i].col < b[j].col) {
				d[k].row = a[i].row;
				d[k].col = a[i].col;
				d[k++].value = a[i++].value;
			}
			else {
				d[k].row = b[j].row;
				d[k].col = b[j].col;
				d[k++].value = b[j++].value;
			}
		}
		else if (a[i].row < b[j].row) {
			d[k].row = a[i].row;
			d[k].col = a[i].col;
			d[k++].value = a[i++].value;
		}
		else {
			d[k].row = b[j].row;
			d[k].col = b[j].col;
			d[k++].value = b[j++].value;
		}
	}
	//fill in the elements that are left
	for (; i <= a[0].value; i++) {
		d[k].row = a[i].row;
		d[k].col = a[i].col;
		d[k++].value = a[i++].value;
	}
	for (; j <= b[0].value; j++) {
		d[k].row = b[j].row;
		d[k].col = b[j].col;
		d[k++].value = b[j++].value;
	}

	d[0].value = k - 1;
}

int main() {

	//matrix a = create(3, 5);

	matrix a = malloc(sizeof(element) * 9);
	a[0].row = 6; a[0].col = 6; a[0].value = 8;
	//matrix b = malloc(sizeof(element)*9)
	a[1].row = 0; a[1].col = 0; a[1].value = 15;
	a[2].row = 0; a[2].col = 3; a[2].value = 22;
	a[3].row = 0; a[3].col = 5; a[3].value = -15;
	a[4].row = 1; a[4].col = 1; a[4].value = 11;
	a[5].row = 1; a[5].col = 2; a[5].value = 3;
	a[6].row = 2; a[6].col = 3; a[6].value = -6;
	a[7].row = 4; a[7].col = 0; a[7].value = 91;
	a[8].row = 5; a[8].col = 2; a[8].value = 28;

	printf("Matrix a:\n");
	smvisualprint(a, false);
	printf("\n");

	matrix b;
	smcreate(&b, 3, 5);
	smfastTranspose(a, b);

	printf("Matrix b: \n");
	smvisualprint(b, false);
	printf("\n");

	matrix d;
	smcreate(&d, 5, 5);
	smadd(a, b, d);

	printf("Matrix a + b: \n");
	smvisualprint(d, false);
	printf("\n");

	free(a);
	smremove(&b);
	free(d);
	return 0;
}
