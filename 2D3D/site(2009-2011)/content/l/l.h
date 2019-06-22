#include <stdio.h>

int main(){
	unsigned long a=1*4+1*5+1*40;
	unsigned long b=((a+1)*4)+((a+1)*5)+((a+1)*40)+a;
	unsigned long c=((b+1)*4)+((b+1)*5)+((b+1)*40)+b;
	unsigned long d=((c+1)*4)+((c+1)*5)+((c+1)*40)+c;
	unsigned long e=((d+1)*4)+((d+1)*5)+((d+1)*40)+d;
	unsigned long f=((e+1)*4)+((e+1)*5)+((e+1)*40)+e;
	unsigned long g=((f+1)*4)+((f+1)*5)+((f+1)*40)+f;
	unsigned long h=((g+1)*4)+((g+1)*5)+((g+1)*40)+g;
	unsigned long i=((h+1)*4)+((h+1)*5)+((h+1)*40)+h;
	unsigned long j=((i+1)*4)+((i+1)*5)+((i+1)*40)+i;
	unsigned long k=((j+1)*4)+((j+1)*5)+((j+1)*40)+j;
	unsigned long l=((k+1)*4)+((k+1)*5)+((k+1)*40)+k;
	printf("1-");
	printf("%lu\n",a);
	printf("%lu-",a+1);
	printf("%lu\n",b);
	printf("%lu-",b+1);
	printf("%lu\n",c);
	printf("%lu-",c+1);
	printf("%lu\n",d);
	printf("%lu-",d+1);
	printf("%lu\n",e);
	printf("%lu-",e+1);
	printf("%lu\n",f);
	printf("%lu-",f+1);
	printf("%lu\n",g);
	printf("%lu-",g+1);
	printf("%lu\n",h);
	printf("%lu-",h+1);
	printf("%lu\n",i);
	printf("%lu-",i+1);
	printf("%lu\n",j);
	printf("%lu-",j+1);
	printf("%lu\n",k);
	printf("%lu-",k+1);
	printf("%lu\n",l);
    printf("%lu-",l+1);
	return 0;
}