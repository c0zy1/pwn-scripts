#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <unistd.h>

// eternalblue as 6 seperated byte arrays

static const uint8_t EternalFraction1[]= {0x65, 0x74};
static const uint8_t EternalFraction2[]= {0x65, 0x72};
static const uint8_t EternalFraction3[]= {0x6e, 0x61};
static const uint8_t EternalFraction4[]= {0x6c, 0x62};
static const uint8_t EternalFraction5[]= {0x6c, 0x75};
static const uint8_t EternalFraction6[]= {0x65};

// struct for one piece of 6 

typedef struct{
    const uint8_t *data;
    size_t len;
} EternalFraction;

// big struct that assembles all the fractions into one big struct

typedef struct{
    EternalFraction parts[6];
} EternalPassword;


// initialize the struct

static const EternalPassword Et = {
        .parts = {
            {EternalFraction1, sizeof(EternalFraction1)},
            {EternalFraction2, sizeof(EternalFraction2)},
            {EternalFraction3, sizeof(EternalFraction3)},
            {EternalFraction4, sizeof(EternalFraction4)},
            {EternalFraction5, sizeof(EternalFraction5)},
            {EternalFraction6, sizeof(EternalFraction6)},
        }
    };

// calculating the length of the password for s3cret function 

size_t length(void){
    size_t sum = 0;
    for (int i = 0; i < 6; i++)
        sum+= Et.parts[i].len;
    return sum;
}

// function to compare byte by byte, used in s3cret()

uint8_t check(size_t idx){
    size_t offset = 0;
    for (int i= 0; i < 6; i++){
        size_t len = Et.parts[i].len;
        if (idx < offset+ len)
            return Et.parts[i].data[idx-offset];
        offset += len;
    }
    return 0;
}

//banner for the calc

void banner(){
    printf("|====================================|\n");
    printf("|             calc.exe               |\n");
    printf("|====================================|\n");
    printf("| [1] Addition                       |\n");
    printf("| [2] Subtraction                    |\n");
    printf("| [3] Multiplication                 |\n");
    printf("| [4] Division                       |\n");
    printf("| [5] Modulo                         |\n");
    printf("| example:  3 2 6 -> 2 * 6           |\n");
    printf("|====================================|\n");
            printf("Select an option: \n\n");
}

//secret flag function


void s3cret(void){
    
    ssize_t n;
    size_t lengthi= length();
    char buf[100];

    printf("do you want to go deeper into the rabbit hole?\n\n");
    printf("give me the key:\n\n");
    
    n = read(0, buf, lengthi+1);
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
    if (buf[n-1] == '\n'){
            n--;
        }
    if (n != lengthi){
        printf("thats not it... go fire up ghidra!\n");
    }else{
        for(size_t i= 0; i < (size_t)n; i++){
            if ( (uint8_t)buf[i] != check(i)){
                return;
            } 
            FILE *f = fopen("flag", "rb");
                if (!f) {
                    perror("fopen");
                    return ;
                }

                char buf[4096];
                size_t n;
                while ((n = fread(buf, 1, sizeof(buf), f)) > 0) {
                    if (fwrite(buf, 1, n, stdout) != n) {
                        perror("fwrite");
                        fclose(f);
                        return ;
                    }
                }
                if (ferror(f)) perror("fread");

                fclose(f);
                return ;
            }
        }

    }

//main logic for the calculator 


int calc(int op, float x , float y){

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
    return 0;
}


int main(){
    int op, input;
    double x, y;
    banner();
    while (1){
        printf(">>>");
        input= scanf("%i %lf %lf", &op, &x, &y );

        if (input== EOF){
            printf("\n bye bye!");
        }
        if (input != 3){
            printf("check the banner!\n");
            int c;
            while ((c= getchar()) != '\n' && c != EOF) {}
            continue;
        }
        if (op == 1337 && x == 42 && y == 7){
            s3cret();
            int c;
            while ((c = getchar()) != '\n' && c != EOF) {}
            continue;
        }
        if (op < 0 || op > 5){
            printf("Operation not permitted!");
            return EXIT_FAILURE;
        }else{
        calc(op, x, y);
        }
    }
    return 0;
}