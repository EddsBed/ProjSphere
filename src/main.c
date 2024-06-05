//Daniel Fredrick May 2024
//This is developed using the ficticious liscence for 
//Employment purposes. UCAR/NCAR has all rights to read, 
//modify, use, or distribute this application

#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>
#include <errno.h>
#include "Foo.h"

//argv takes in a string from the OS. Globbing may mess with input
int main(int argc, char *argv[]){

    //Ensure input is one passed argument in addition to the function call argument in argv[0]
    if(argc != 2){
            fprintf(stderr, "Error: Expected 2 arguments. Received %d\n", argc);
            errno = EINVAL;
            return(EXIT_FAILURE);
    }

    //Ensure input argument is valid while converting it to a double
    //Succeptible to overflow and potential buffer attacks, 
    char *endInput;
    double radius = strtod(argv[1], &endInput);
    if(*endInput != '\0'){
        fprintf(stderr, "Error, invalid input");
        errno = EINVAL;
        return(EXIT_FAILURE);
    }

    //Perform the volume calculation V= (4/3)pi*r^3
    double volume= Foo(radius);

    //Check if volume calculation succeeded
    if(volume == EXIT_FAILURE){
        return EXIT_FAILURE;
    }
    else{
        printf("%.32lf\n", volume);
    }
    
    return EXIT_SUCCESS;
}