//Vowels And Consonants
%{
#include<stdio.h>
    int vct=0,naatct=0;
%}

%%
[aeiouAEIOU] {vct++;}  printf("vowel");
.+           {naatct++;} printf("Naat");
%%

int main()
{
    yylex();
    printf("vowel=%d not=%d",vct,naatct);
    return 0;
}
