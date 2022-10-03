
#pragma once
#include "Listabarquito.h"
class Nodocategorias{
public:
        std::string categoria;
        Listabarquito* Barcos;
        Nodocategorias* siguienteNodo;
        Nodocategorias* anteriorNodo;
public:


    Nodocategorias(std::string categoria){
        this->categoria = categoria;
        this->Barcos = new Listabarquito();
        this->siguienteNodo = NULL;
    }

    Nodocategorias(){
        this->categoria="";
        this->Barcos = NULL;
        this->siguienteNodo = NULL;
    }

};
