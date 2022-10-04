
#pragma once
#include <iostream>

class Barco {
public:
    int id;
    int precio;
    std::string nombre;
    std::string categoria;
    std::string src;
    bool comprado;
public:
    Barco(int id, int precio, std::string nombre, std::string categoria, std::string src,bool comprado){
    this->id = id;
    this->precio = precio;
    this->nombre = nombre;
    this->categoria = categoria;
    this->src = src;
    this->comprado = comprado;
    }
    Barco(){
    this->id = 0;
    this->precio = 0;
    this->nombre = "";
    this->categoria = "";
    this->src = "";
    this->comprado = false;
    }
~Barco(){ //*Destructor

    }
void mostrar(){
    std::cout<<"Id: "<<this->id<<", precio: "<<this->precio<<", nombre: "<<this->nombre<<", src: "<<this->src;
}
};
