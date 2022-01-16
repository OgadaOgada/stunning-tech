#include <iostream>
#include <stack>
using namespace std;
int main(){

stack<string> countries;
countries.push("Delhi");
countries.push("Kenya");
countries.push("Egypt");
countries.push("Nigeria");

while (!countries.empty()){
    count<<" " << countries.top();
    countries.pop();
}

}