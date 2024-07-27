#include<iostream>
using namespace std;
int countdigit(int n);
int armstrong(int n, int digit);
int main(){
    int num;
    cout<<"Enter a number : ";
    cin>>num;
    int digit = countdigit(num);
    int armstong = armstrong(num,digit);
    return 0;
}