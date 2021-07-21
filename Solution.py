/*#include <iostream>
using namespace std; //header file
int main(){ // main function

    float m,cm; //declare variable

    cout<<"Enter the value of meter";
    cin>>m;
    cout<<"Enter the value of centimeter";
    cin>>cm; // store value

    cout<<"The value in meter is ";
    cout<<m*100<<endl; //displaying the results

    cout<<"The value in centimeter is ";
    cout<<cm / 100;
}
*/
---------------------------------------------------------

/*#include <iostream>
using namespace std;

int main(){

    cout<<"Size of Char : "<<sizeof(char)<<" byte"<<endl;
    cout<<"Size of Integer : "<<sizeof(int)<<" byte"<<endl;
    cout<<"Size of Short Interger : "<<sizeof(short int)<<" byte"<<endl;
    cout<<"Size of Long Integer: "<<sizeof(long int)<<" byte"<<endl;
    cout<<"Size of Signed Long Integer : "<<sizeof(signed long int)<<" byte"<<endl;
    cout<<"Size of Float : "<<sizeof(float)<<" byte"<<endl;
    cout<<"Size of Double : "<<sizeof(double)<<" byte"<<endl;
    cout<<"Size of wchar_t  : "<<sizeof(wchar_t)<<" byte"<<endl;

    return 0;

}
*/
---------------------------------------------------------

/*#include <iostream>
using namespace std;

int main(){

    int number;
    cout<<"Enter an integer"<<endl;
    cin>>number;

    if (number > 0){
        cout<<"You entered a positie integer :"<<number<<endl;
    }
    cout<<"This is a default Statement";
    return 0;

}*/

---------------------------------------------------------

/*#include <iostream>
using namespace std;

int main(){

    int number;
    cout<<"Enter an integer"<<endl;
    cin>>number;

    if (number > 0){
        cout<<"You entered a positive integer : "<<number<<endl;
    }
    else{
        cout<<"You entered a negative integer : "<<number<<endl;
    }
    return 0;

}*/
---------------------------------------------------------

// If the Enter number is odd or even

/*#include <iostream>
using namespace std;

int main(){

    int num ;
    cin >> num;
    if (num % 2 != 0){
        cout<<"Given number is odd number";
    }
    else{
        cout<<"Given number is the even number";
    }
    return 0;
}
*/

---------------------------------------------------------


// To check wheather the number is positive , negative or 0

/*#include <iostream>
using namespace std;

int main(){

    int number;
    cout << "Enter a number";
    cin >> number;

    if (number > 0){
        cout << " The given number is positive";
    }
    else if (number < 0){
        cout << " The entered number is negative";
    }
    else{
        cout << "You entered 0";
    }

}
*/
---------------------------------------------------------

// Divisibility factor of a number

/*#include <iostream>
using namespace std;

int main(){

    int a ;
    cout << "Enter a number";
    cin >> a;

    if (a % 5 == 0 && a % 8 == 0){
        cout <<"The entered number is divisible by 5 and 8" << endl;
    }
    else if (a % 8 == 0){
        cout <<"The entered number is divisible by 8" << endl;
    }
    else if (a % 5 == 0){
        cout <<"The entered number is divisible by 5" << endl;
    }
    else {
        cout<<"The entered number is divisible by none";
    }
    return 0;
  }
---------------------------------------------------------


// To check wheather the entered integer is even and odd

/*#include <iostream>
using namespace std;

int main(){

    int num;
    cout << "Enter an integer";
    cin >> num;

    //outer if condition
    if (num != 0){
        //inner if condition
        if ((num % 2) == 0){
            cout << "The number is even"<<endl;
        }
        // inner else condition
        else{
            cout << "The number is odd" <<endl;
        }
    }
    // outer else condition
    else{
        cout << " The number is zero and its neither even or odd"<<endl;
    }
    return 0;
}
---------------------------------------------------------

// To check wheather which number is greater out of 3 number


/* #include <iostream>
using namespace std;

int main()
{
    int a, b, c;
    cout << "Enter 3 numbers : ";
    cin >> a >> b >> c;
    if (a > b)
    {
        if (a > c){
            cout << "The first number is greatest" <<endl;
        }
        else{
            cout << " The third number is the greatest" <<endl;
        }
    }
    else if (b > c){
        cout << "The second number id the greatest" << endl;
    }
    else{
        cout << " The third number is the greatest" <<endl;
    }
    return 0;
}
---------------------------------------------------------


// To check the student is passed or failed his examination

/*#include <iostream>
using namespace std;

int main(){

    int marks;
    cout<<"Eter your marks: ";
    cin >> marks;

    if (marks >= 50){
        cout << " Congrats, You have passed"<<endl;
        if (marks == 100){
            cout<<"Perfect";
        }
    }
    else{
        cout << "You have failed" << endl;
    }
}
---------------------------------------------------------

//Making of a Calculator

/*
#include <iostream>
using namespace std;

int main()
{
    char oper;
    float num1, num2;
    cout << "Enter an operator(+ , - , * , / ) : ";
    cin >> oper;
    cout << "Enter two number: "<<endl;
    cin >> num1 >> num2;

    switch(oper){
    case '+':
        cout << num1 + num2 <<endl;
        break;
    case '-':
        cout << num1 - num2 <<endl;
        break;
    case '*':
        cout << num1 - num2 <<endl;
        break;
    case '/':
        cout << num1 / num2 <<endl;
        break;
    default:
        cout << "Error! The operator is incorrect" <<endl;
    }
    return 0;
}
---------------------------------------------------------


//To raise number m by n and taking default value as  2 if vaulue of n is not entered

/*
#include <iostream>
using namespace std;

void power(double base, int exp = 2)
{
    double ans = 1;
    for (int i = 1; i <= exp; i++)
    {
        ans =  ans*base;
    }
    cout << ans;
}

int main()
{
    int n;
    double m;
    char ch;
    cout << "Enter a base value"<<endl;
    cin >> m;
    cout<<" Do you want a exponent Value (Y/N) : "<<endl;
    cin>>ch;
    if ((ch == 'y') || (ch == 'Y')){
        cout<<"Enter exponent Value : "<<endl;
        cin >> n;
        power(m,n);
    }
    else{
        power(m);
    }
    return 0 ;
}

---------------------------------------------------------

/*

Pyramid Construction
*
**
***
****
*****

*/

/*
#include <iostream>
using namespace std;

int main()
{
    int rows;
    cout<<"Enter the number of rows"<<endl;
    cin >> rows;

    for(int i = 1; i <= rows; ++i){
        for (int j = 1; j <= i; ++j ){
            cout<<"*";
        }
        cout << "\n";
    }
    return 0;
}

---------------------------------------------------------


/*

Pyramid Construction
A
BB
CCC
DDDD
EEEEE

*/

/*
#include <iostream>
using namespace std;

int main()
{
    char  input, alphabet = 'A';
    cout<<"Enter the times";
    cin >> input;

    for(int i = 1; i<= 5; ++i){
        for (int j = 1; j<= i; ++j ){
            cout<<alphabet<<" ";
        }
        ++alphabet;
        cout <<endl;
    }
    return 0;
}

---------------------------------------------------------


//Pascal Triangle

/*
#include <iostream>
using namespace std;

int main()
{
    int rows, coef = 1;
    cout<<"Enter the number of rows: ";
    cin >> rows;

    for(int i = 0; i< rows; i++)
    {

        for (int space = 1; space <= rows - i; space++)
            cout<<"  ";


        for(int j = 0; j <= i; j++){
            if(j == 0 || i == 0)
                coef = 1;
            else
                coef =  coef*(i - j + 1)/j;
            cout << coef << "  ";
        }
        cout << endl;
    }
    return 0;
}

---------------------------------------------------------

/*
Pyramid Construction
1
2 3
4 5 6
7 8 9 10

*/

/*
#include <iostream>
using namespace std;

int main()
{
    int rows, number = 1;
    cout << "Enter the number of rows ";
    cin >> rows;

    for(int i = 1; i <=rows; i++){
        for(int j = 1; j<= i; j++ ){
            cout<<number<<" ";
            ++ number;
        }
        cout << endl;
    }
     return 0;
}
---------------------------------------------------------

// While Loop

//sum of positive number only

/*
#include <iostream>
using namespace std;

int main(){
    int number, sum = 0;
    cout<<"Enter the number";
    cin >> number;

    while(number > 0)
    {
        sum += number;
        cout<<"Enter a number: ";
        cin >> number;

    }
    cout << "\n The sum is "<<sum<<endl;
    return 0;
}
---------------------------------------------------------


//Printing Hello World

/*
#include<iostream>
using namespace std;

int main()
{
    int i = 0, n;
    cout << "How many times do you want to get printed";
    cin >> n;

    while(i < n)
    {
        cout <<"Hello World"<<endl;
        i++;
    }
    return 0;
}
---------------------------------------------------------


// to demostrate * pattern using while loop

/*
#include <iostream>
using namespace std;

void pyramid(int n)
{
    int i = 0;
    int j = 0;
    int k = 0;
    while(i < n)
    {
        while(k <= n-i-2)
        {
            cout<<" ";
            k++;
        }
        k = 0;
        while(j < 2*i-1)
        {
            cout<<"*";
            j++;
        }
        j = 0;
        i++;
        cout<<endl;
    }
}


int main()
{
    int n;
    cin>>n;
    pyramid(n);
    return 0; 
}
*/
