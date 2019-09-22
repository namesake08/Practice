//Write the program which is count parallelogram area.
#include <stdio.h>
#include <conio.h>

void main()
{
     float l, w; //lenght and width
     float s;    //square

     printf("\nCounting a parallelogram or rectangle square\n");
     printf("Enter the data:\n");
     printf("Lenght ->  ");
     scanf("%f", &l);
     printf("Width ->  ");
     scanf("%f", &w);
     s = l * w;
     printf("Parallelogram square is: %1.2f sq. c.(for ex.)\n", s);

     printf("\n\nPress any button to exit");
     getch();
}
