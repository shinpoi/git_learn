// gcc -o np_array_sum.so -shared -fPIC np_array_sum.c

// 1-dim array.  a[] -> array, n -> long of array
double mysum1(double a[], long n){
	double sum = 0;
	long i;
	for(i=0; i<n; i++){
		sum += a[i];
	}
	return sum;
}

// 2-dim array
double mysum2(double a[], long strides[], long shape[]){
	double sum = 0;
	long i,j,M,N,S0,S1;
	M = shape[0]; N = shape[1];
	S0 = strides[0] / sizeof(double);
	S1 = strides[1] / sizeof(double);

	for(i=0; i<M; i++){
		for(j=0; j<N; j++){
			sum += a[i*S0 + j*S1];
		}
	}

	return sum;
}
