%{
#include<stdio.h>
    int p=0,n=0;
    
%}
Pnum [+]?[0-9]
Nnum [-]?[0-9]

%%
{Pnum}+ {p++;  printf("positive");}
{Nnum}+ {n++;  printf("Negative");}
%%

int main()
{
    printf("Enter Numbers:");
    yylex();
    printf("Positive=%d Negative=%d",p,n);
    return 0;
}

