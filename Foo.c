#include <math.h>
#include <stdio.h>
#include <stdlib.h>


#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

int main(int argc, char *argv[]){
    if(argc != 2){
            fprintf(stderr, "Error: Expected 2 arguments. Received %d\n", argc);
            exit(EXIT_FAILURE);
    }
    //converts the argument into a double.
    //atof is vulnerable to potential out of bounds or malicious input. Consider using strtod.
    double radius = atof(argv[1]); 

    //M_PI is limited to double floating precision as outlined with POSIX 
    double volume = pow(radius, 3.0)*(4*M_PI/3);

    printf("%lf\n", volume);
    return EXIT_SUCCESS;



}