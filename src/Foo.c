#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <signal.h>

static double coefVal= (double)(M_PI/3.0); ;

double Foo(double radius){
   
    //M_PI is limited to double floating precision as outlined with POSIX 
    double volume = pow(radius, 3.0) * coefVal;
    // printf("%.15lf\n", coefVal);
    // printf("%lf\n", volume);
    return volume;
}