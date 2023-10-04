#include <stdio.h>
int main()
{
    float a, b;
    int c;
    printf("Enter first number : ");
    scanf("%f", &a);
    printf("\nEnter second number : ");
    scanf("%f", &b);
    printf("1. +\n2. -\n3. *\n4. /\nPlease choose number assigned to your operator :");
    scanf("%d", &c);
    if (c==1)
    {
    printf("\nSum is %f", a+b);
        
    }
    else if (c==2)
    {
    printf("\nDifference is %f", a-b);
    }
    
    else if (c==3)
    {
    printf("\nProduct is %f", a*b);
        
    }
    
    else if (c==4)
    {
    printf("\nDivide is %f", a/b);
        
    }

    else
    {
        printf("\nPlease a valid operator");
    }

    return 0;
}
