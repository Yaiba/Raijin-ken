#include <stdio.h>

int target[10] = {10,9,8,7,6,5,4,3,2,1};

void swap(int i, int j) {
    int tmp;
    tmp = target[i];
    target[i] = target[j];
    target[j] = tmp;
}

void quick(int left, int right) {
    printf("[ %d - %d ]\n", left, right);
    if (left > right)
        return;
    int flag = target[left], i=left, j=right;
    while (i != j) {
        printf("%d + %d\n", i, j);
        while((target[j] >= flag) && (j > i))
            j--;
        while((target[i] <= flag) && (j > i))
            i++;
        if (j > i)
            swap(i, j);
    }
    // i meet j
    swap(left, j);
    quick(left, i-1);
    quick(i+1, right);
}

int main() {
    int i, j, temp;
    for(i=0;i<10;i++) {
        printf("%d ", target[i]);
    }
    printf("\n");

    quick(0, 9);

    for(i=0;i<10;i++) {
        printf("%d ", target[i]);
    }
    printf("\n");
}
