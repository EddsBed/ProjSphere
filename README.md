# ProjSphere
This is a repository to host my personal development of a Sphere software package. The core requirement for this package is to calculate the volume given it's radius.  This is made for an employment assignment given from NCAR

This application calculates the volume of a sphere given a radius. This radius is expected to be a single numerical value that is constant across the shape. This application ahderes to the limitations of the 64 bit double precision IEE 754 variable which C uses. Modifications to make calculations more accurate are possible in the future. 

In order to compile, type make. The executable will be called Foo in your /bin directory. This is indented to follow some variant of the POSIX standard and gcc. 

Usage: ./Foo [number] Will output the volume Following the calculation to stdout. 

Tests: 
If you wish to verify this code, a test framework is provided. 
Usage: python3 run_tests.py