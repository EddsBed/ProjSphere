#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include "Foo.h"

int main(int argc, char *argv[]){
    if(argc != 2){
            fprintf(stderr, "Error: Expected 2 arguments. Received %d\n", argc);
            exit(EXIT_FAILURE);
    }
    //converts the argument into a double.
    //atof is vulnerable to potential out of bounds or malicious input. Consider using strtod.
    double radius = atof(argv[1]); 
    double volume= Foo(radius);
    printf("%.32lf\n", volume);
    return EXIT_SUCCESS;
}