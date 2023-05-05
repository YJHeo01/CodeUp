#include <stdio.h>

int main()
{
    int n;
    scanf("%d",&n);
    int money[8] = {50000,10000,5000,1000,500,100,50,10};
    int cnt = 0;
    int index = 0;
    while(n!=0)
    {
        if(n-money[index]>=0)
        {
            n -= money[index];
            cnt++;
        }else{
            index++;
        }
    }

    printf("%d",cnt);

    return 0;
}
