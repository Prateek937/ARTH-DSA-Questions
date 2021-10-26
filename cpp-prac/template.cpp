#include<iostream>

// Writing the prototype of the template
template <typename T>
T addition(T num1, T num2);

int main(){
    int x;
    int y;
    double dx;
    double dy;
    std::cout<<"Enter interger x and y: ";
    std::cin>>x>>y;
    std::cout<<"Enter double dx and dy: ";
    std::cin>>dx>>dy;

    // Calling template with different datatypes
    std::cout<<"Interger addition: "<<addition<int>(x,y)<<std::endl;
    std::cout<<"Double addition: "<<addition<double>(dx, dy)<<std::endl;
    
    std::endl(std::cout); // For a new line
    
    return 0;


}

// Defining a template of a function
template <typename T>
T addition(T num1, T num2){ 
    return num1+num2;
}

