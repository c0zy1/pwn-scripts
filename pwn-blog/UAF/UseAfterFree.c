#include <stdlib.h>

int main(){
    char *p= malloc(8);
    free(p);
    gets(p);
    puts(p);
}