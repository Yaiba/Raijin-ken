#include <stdio.h>
// time: O(2*(m+n)) -> O(M+N)

int main() {
    int target[1000], i, j ,t, n;

    for (i=0; i <= 1000; i++)
        target[i] = 0;

    printf("input the item num, then the item\n");
    // input the num of item to receive
    scanf("%d", &n);

    for (i=0; i < n; i++) {
      scanf("%d", &t);
      target[t]++;
    }

    printf("\n");

    for (i=0; i <= 1000; i++)
      for (j=0; j < target[i]; j++)
        printf("%d ", i);

    getchar();
    getchar();
    return 0;
}

