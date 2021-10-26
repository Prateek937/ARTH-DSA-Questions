#include "iostream"
int addition(int num1, int num2);
double addition(double num1, double num2);


int main(){
    int x;
    int y;
    double dx;
    double dy;
    std::cout<<"Enter interger x and y: ";
    std::cin>>x>>y;
    std::cout<<"Enter double dx and dy: ";
    std::cin>>dx>>dy;

    std::cout<<"Interger addition: "<<addition(x,y)<<std::endl;
    std::cout<<"Double addition: "<<addition(dx, dy)<<std::endl;
    
    return 0;


}

// Creating the functions with same name but different datatype and parameters.
int addition(int num1, int num2){
    return num1+num2;
}

double addition(double num1, double num2){
    return num1+num2;
}
