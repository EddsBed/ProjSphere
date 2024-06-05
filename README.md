# Foo
An assignment that calculates the volume of a sphere. 

### Calculation
This program uses IEEE 754 to store its values. This is a 64 bit double precision floating point number.  
Due to the modularity of this code, a higher precision module may be added in the future.

The area of a sphere can be calculated using the formula:
$$Volume = \frac{4} {3} \pi Radius^3$$

### Usage
This program was written and tested using gcc. It is indended to be POSIX-compliant. 
To compile this program, run the command 'make' in the root directory. The compiled binaries will appear in ~/bin. 

To run the command in the bin directory, type ```./Foo [number]``` Replace [number] with your desired value. 
This application does not directly support any type of input other than a single static real number. All calculations needed to create such must be done beforehand. 
Provided a correct input, the number will be returned to stdout. If no number is returned then the executable has failed. The error is printed to stderr.

### Examples 

```     $ ./Foo 3``` 

stdout: 28.27433388230813449126799241639674



```     $ ./Foo 212.645``` 

stdout: 10069180.92252221144735813140869140625000

### Testing 
A framework for testing in python has been created. Four lists of test options have been created: 
    ```TcBoundsSucceed = [[]]```
    ```TcBoundsFail = [[]]```
    ```TcParsingSucceed = [[]]```
    ```TcParsingFail = [[]]```

    
To populate them, enter your input and desired output as follows: ```TcBoundsSucceed = [['input', output_min, output_max],['input2',output2_min,output2_max]}```
For each element of the passing lists should be a list of size three. The first element should be the string representation of the input number ie '3.0'. The next two elements specify the range of accepted values. 
You are required to set a range as rounding errors and limitations may exist due to the nature of C. 
The python code will iterate through and test every valid entry in each array.  
An example of a successful bounds testing: ```TcBoundsSucceed = [['3',28.27433388230813449126799241639674, 28.27433388230813449126799241639675]]```
To run the tests, type: ```python3 run_tests.py``` in the root directory.
