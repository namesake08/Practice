#include <stdio.h>
#include <unistd.h>

int main(int argc, char *argv[])
{
   int i;

   if(argc < 2)
   {
      printf("You didn't specify the arguments or parameters\n");
      exit(1);
   }
   
   if (write(1, "This will be output to standard out\n", 36) != 36) {
        write(2, "There was an error writing to standard out\n", 44);
        return -1;
    }
   return(0);
}