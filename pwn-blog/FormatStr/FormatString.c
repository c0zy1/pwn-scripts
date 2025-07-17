#include <stdio.h>
#include <string.h>

int main(int argc, char **argv){
    char name[32];
    strcpy(name, argv[1]);
    printf(name);
}