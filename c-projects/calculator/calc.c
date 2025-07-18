#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h> 



void banner(){
    printf("|====================================|\n");
    printf("|             calc.exe               |\n");
    printf("|====================================|\n");
    printf("| [1] Addition                       |\n");
    printf("| [2] Subtraction                    |\n");
    printf("| [3] Multiplication                 |\n");
    printf("| [4] Division                       |\n");
    printf("| [5] Modulo                         |\n");
    printf("| [0] Exit                           |\n");
    printf("| example: calc.exe 3 2 6 -> 2* 6    |\n");
    printf("|====================================|\n");
            printf("Select an option: \n\n");
}

int calc(int op, float x , float y){
    if (op < 1 || op > 5 ){
        printf("Operation not permitted!");
    return EXIT_FAILURE;
    }
    else{
    float result;
    switch (op){
        case 1 : result = x + y ; break;
        case 2 : result = x - y ; break;
        case 3 : result = x * y ; break;
        case 4 : 
            if (y == 0){
                fprintf(stderr, "Error: Division durch Null!\n");
            }
            result = x / y ; break;
        case 5: 
            result = (int)x % (int)y ; break; 
    }
    printf("Result %.2f\n", result);
    return EXIT_SUCCESS;
}
}


int main(int argc, char *argv[]){
    banner();
    double x = atof(argv[2]);
    double y = atof(argv[3]);
    int op = atoi(argv[1]);
    calc(op, x, y);
    return 0;
}