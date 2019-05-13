#include <unistd.h>
 #include <stdio.h>
 using namespace std;

extern "C" void open_pin() {
	FILE *export_file = NULL; 
	char str[] = "60"; 
	export_file = fopen ("/sys/class/gpio/export", "w");
	fwrite (str, 1, sizeof(str), export_file);
	fclose (export_file);
}

extern "C" void close_pin() {
	FILE *export_file = NULL;
	char str[] = "60";
	export_file = fopen ("/sys/class/gpio/unexport", "w");   //remove the mapping
	fwrite (str, 1, sizeof(str), export_file);
	fclose (export_file);
}

extern "C" void turn_on() {
	 FILE *IO_direction = NULL;
	char high[] = "high";
	 IO_direction = fopen ("/sys/class/gpio/gpio60/direction", "w");
	fwrite (high, 1, sizeof(high), IO_direction);   //set the pin to HIGH
         fclose (IO_direction);
}

extern "C" void turn_off() {
	 FILE *IO_direction = NULL;
	 char low[] = "low";
	IO_direction = fopen ("/sys/class/gpio/gpio60/direction", "w");
	fwrite (low, 1, sizeof(low), IO_direction);   //set the pin to low
	fclose (IO_direction);
}	

 int main()
 {
         FILE *export_file = NULL;        //declare pointers
         FILE *IO_direction = NULL;
         char str1[] = "low";
         char str2[] = "high";
         char str[] = "60";                       //value to pass to export file
         export_file = fopen ("/sys/class/gpio/export", "w");
         fwrite (str, 1, sizeof(str), export_file);
         fclose (export_file);


 for (int i=0; i<10; i++){        //blink LED 10 times
         IO_direction = fopen ("/sys/class/gpio/gpio60/direction", "w");
         fwrite (str2, 1, sizeof(str1), IO_direction);   //set the pin to HIGH
         fclose (IO_direction);
         usleep (1000000);

         IO_direction = fopen ("/sys/class/gpio/gpio60/direction", "w");
         fwrite (str1, 1, sizeof(str1), IO_direction);   //set the pin to LOW
         fclose (IO_direction);
         usleep (1000000);}

         export_file = fopen ("/sys/class/gpio/unexport", "w");   //remove the mapping
         fwrite (str, 1, sizeof(str), export_file);
         fclose (export_file);
 }
