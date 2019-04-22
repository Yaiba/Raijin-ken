#include <stdio.h>
// time: O(N^2)

int main() {
    int i,j,tmp,n;
    scanf("%d", &n);
    int target[n];
    for(i=0; i < n; i++)
      scanf("%d", &target[i]);

    printf("input done.\n");

    for(i=0; i < n-1; i++) {
      for(j=0; j < n-i; j++){
          if (target[j] < target[j+1]) {
              tmp = target[j];
              target[j] = target[j+1];
              target[j+1] = tmp;
          }
      }
    }

    for(i=0; i < n; i++)
      printf("%d ", target[i]);

    printf("\n");

    getchar();
    getchar();
    return 0;
}
