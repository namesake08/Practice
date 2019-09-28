#include <stdio.h>	//inlcude directive tells the preprocessor to insert the contents of another file at the point where the include directive is found
#include <limits.h>	//giving below is an example to get the size of various type of a machine using different constant defined in limits.h header file
#include <stdlib.h>

int main(int argc, char** argv)
{
    printf("CHAR_BIT	:    %ld\n", CHAR_BIT);
    printf("CHAR_MAX	:    %ld\n", CHAR_MAX);
    printf("CHAR_MIN	:    %ld\n", CHAR_MIN);
    printf("INT_MAX     :    %ld\n", INT_MAX);
    printf("INT_MIN     :    %ld\n", INT_MIN);
    printf("LONG_MAX	:    %ld\n", (long) LONG_MAX);
    printf("LONG_MIN    :    %ld\n", (long) LONG_MIN);
    printf("SCHAR_MAX   :    %d\n", SCHAR_MAX);
    printf("SCHAR_MIN   :    %ld\n", SCHAR_MIN);
    printf("SHRT_MAX    :    %d\n", SHRT_MAX);
    printf("SHRT_MIN    :    %d\n", SHRT_MIN);
    printf("UCHAR_MAX   :   %d\n", UCHAR_MAX);
    printf("UINT_MAX    :   %u\n", (unsigned int) UINT_MAX);
    printf("ULONG_MAX   :   %lu\n", (unsigned long) ULONG_MAX);
    printf("USHRT_MAX   :   %d\n", (unsigned short) USHRT_MAX);


    return 0;
}
