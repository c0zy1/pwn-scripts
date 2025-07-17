#include <stdlib.h>
#include <unistd.h> // read()

int main(int c, char** argv){
    size_t n = atoi(argv[1]);
    char *p = malloc(n * 4);
    read (0, p, n* 4);
}