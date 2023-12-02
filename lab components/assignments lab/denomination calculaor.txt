#include <stdio.h>

void calc(int amount, int d[], int n);

void input() {
    int a;
    printf("Enter total: ");
    scanf("%d", &a);

    int d[3];
    printf("Enter denominations: ");
    for (int i = 0; i < 3; i++) {
        scanf("%d", &d[i]);
    }

    printf("Total: %d\n", a);
    printf("Denominations: ");
    for (int i = 0; i < 3; i++) {
        printf("%d ", d[i]);
    }
    printf("\n");

    calc(a, d, 3);
}

void calc(int amount, int d[], int n) {
    if (amount > 0) {
        for (int i = 0; i < n; i++) {
            if (amount >= d[i]) {
                int num = amount / d[i];
                printf("%d X %d\n", d[i], num);
                amount -= d[i] * num;
                printf("Remaining: %d\n", amount);
            }
        }
    }
}

int main() {
    printf("Calculator\n");
    input();
    return 0;
}