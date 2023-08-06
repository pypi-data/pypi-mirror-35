#include <stdio.h>
//#include "iacaMarks.h"
void dummy(float* a);

int main(void){
    printf("OSACA test start\n");
    int i = 1;
    float arr[1000];
    float tax = 0.19;
    arr[0] = 0;
    i++;
    //STARTLOOP
    while(i < 1000){
        arr[i] = arr[i-1]+i*tax;
        i += 1;
    }
    dummy(&arr[999]);
    printf("OSACA test end\n");
    return 0;
}
