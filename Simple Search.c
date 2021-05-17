#include<stdio.h>
int main()
{
	int N,K,i;
	scanf("%d",&N);
	int A[N];
	for ( i = 0 ; i < N ; i++)
	{
		scanf("%d",&A[i]);
	}
	scanf("%d",&K);
	for ( i = 0 ; i < N ; i++)
	{
		if (A[i] == K)
		{
			printf("%d",i);
		}       
	}

}
