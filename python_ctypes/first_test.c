// gcc -o libpy.so -shared -fPIC first_test.c

#include <stdio.h>  
#include <stdlib.h>  

long summ(long num){
	long i;
	long sum = 0;
	for(i=0; i<num; i++){
		if (i%2==0) {
			sum += i;
		}
		else {
			sum += -i;
		}
	}
	return sum;
}  
