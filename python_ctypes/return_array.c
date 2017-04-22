void plus_array(long a[], long n){
	long i;
	for(i=0; i<n; i++){
		a[i] += 1;
	}
}

long* plus_array2(long a[], long n){
	long i;
	static long b[20];
	
	for(i=0; i<n; i++){
		b[i] = a[i]+1;
	}
	return b;
}
