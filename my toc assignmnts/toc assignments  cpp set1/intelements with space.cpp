#include <stdio.h>

int main() {
    int num;

    printf("Enter numbers (type space to stop):\n");

    while (scanf("%d",&num)==1) {

        int result = num;


        printf("%d\n", result);
    }

    return 0;
}
