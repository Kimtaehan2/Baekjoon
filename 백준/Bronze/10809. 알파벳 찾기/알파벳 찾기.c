#include <stdio.h>
int f(char* pstr, int n)
{
    for (int j = 0; *pstr!='\0'; j++)
    {
        if (n == *pstr)
            return j;
        pstr += 1;
    }
    return -1;
}
int main()
{
    char str[101];
    char* pstr = &str;
    scanf("%s", str, 101);
    for (int i = 0; i < 26; i++)
    {
        printf("%d ", f(pstr, i + 97));
    }
    return 0;
}