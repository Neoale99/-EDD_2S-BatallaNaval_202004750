
#pragma once
#include "Barco.h"

class Nodobarquito{
public:
        Barco* barquito;
        Nodobarquito* siguienteB;
public:
    Nodobarquito(){
        this->barquito = NULL;
        this->siguienteB = NULL;
        }
    Nodobarquito(int id, int precio, std::string nombre, std::string categoria, std::string src,bool comprado){
        this->barquito = new Barco(id, precio, nombre, categoria, src, comprado);
        this->siguienteB = NULL;
    }


};

