/*
 * Apply cellular automata rule to the input array
 * return updated one.
 *
 * Tong Zhang <zhangt@frib.msu.edu>
 * 2018-08-19 21:30:24 EDT
 *
 */

#include "evolve.h"

int main(int argc, char **argv) {
  // int n = 9, ncol = 3, nrow = 3;
  // int a[9] = {1,0,1,0,1,0,0,0,1};

  int n = 250000, ncol = 500, nrow = 500;
  int a[250000] = {0};
  for (int i = 125000; i < 126000; i++)
    a[i] = 1;

  int *new_a = update_pattern(a, n, nrow, ncol);

  // print_pattern(a, n, ncol);
  print_pattern(new_a, n, ncol);

  free(new_a);
  return 0;
}

void print_pattern(int *a, int n, int ncol) {
  for (int i = 0; i < n; i++) {
    if (!(i % ncol))
      printf("\n");
    printf("%d ", a[i]);
  }
  printf("\n");
}

int *update_pattern(int a[], int n, int nrow, int ncol) {
  int *new_a = (int *)malloc(n * sizeof(int));
  int idx_row_low, idx_row_high, idx_col_low, idx_col_high;
  int k;
  int n_neighbors;
  for (int i = 0; i < nrow; i++) {
    for (int j = 0; j < ncol; j++) {
      k = i * ncol + j;
      n_neighbors = -a[k];
      idx_row_low = (i - 1 < 0) ? 0 : (i - 1);
      idx_row_high = (i + 2 > nrow) ? nrow : (i + 2);
      idx_col_low = (j - 1 < 0) ? 0 : (j - 1);
      idx_col_high = (j + 2 > ncol) ? ncol : (j + 2);
      //            printf("Neighbors of [%d](%d, %d)(including me): \n", k, i,
      //            j);
      for (int ii = idx_row_low; ii < idx_row_high; ii++)
        for (int jj = idx_col_low; jj < idx_col_high; jj++)
          //                    printf("  (%d, %d)\n", ii, jj);
          n_neighbors += a[ii * ncol + jj];
      //            printf("\n");
      if (a[k]) {
        if ((n_neighbors < 2) || (n_neighbors > 3)) {
          new_a[k] = 0;
        } else {
          new_a[k] = a[k];
        }
      } else {
        if (n_neighbors == 3) {
          new_a[k] = 1;
        } else {
          new_a[k] = a[k];
        }
      }
    }
  }

  return new_a;
}
