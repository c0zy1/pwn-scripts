#include <stdlib.h>
#include <stdlib.h>
#include <stdio.h>

int main(){
    char *p= malloc(8);
    free(p);
    fgets(p);
    puts(p);
}