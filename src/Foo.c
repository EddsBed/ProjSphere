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

//All constants in the equation are pre calculated for simplicity
static double coefVal= (double)(M_PI/3.0); 

double Foo(double radius){
   
   //Error Check if negative
   if (radius < 0){
    errno = EINVAL;
    fprintf(stderr, "Error: Received negative number");
    return EXIT_FAILURE;
   }

    //M_PI is limited to double floating precision as outlined with POSIX 
    //V= (4/3)pi*r^3
    double volume = pow(radius, 3.0) * coefVal;
    
    return volume;
}