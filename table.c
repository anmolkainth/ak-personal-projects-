#include<stdio.h>
int main()
{
    int a, b=0 , i=0 ;
    printf("Enter your number : ");
    scanf("%d", &a);
    for (;i<11 ;i++, b+a)
    {
        printf("\n%d X %d = ",a,i);
        printf("%d",b);
        b = b+a;
    }
    

}