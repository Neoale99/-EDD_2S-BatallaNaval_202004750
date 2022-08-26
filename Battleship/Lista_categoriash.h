
#pragma once
#include <iostream>
#include "nodocategoria.h"
#include "Listabarquito.h"
class Lista_categoria{
public:
    Nodocategorias* Iniciocate; //Cabecera
    Nodocategorias* Fincate;
    int largodela;
public:
    bool vacio(){
        return Iniciocate == NULL;
    }
    bool buscar(std::string categoria){
        if(vacio()){
            return false;
        }
        Nodocategorias* aux = Iniciocate;
        while(aux!=NULL){
            if(aux->categoria.compare(categoria)==0){
                return true;

            }
            aux = aux->siguienteNodo;

        } return false;
    }
    Nodocategorias* obtener(std::string categoria){
        if(vacio()){
            return NULL;
        }
        Nodocategorias* aux = Iniciocate;
        while(aux!=NULL){
            if(aux->categoria.compare(categoria)==0){
                return aux;

            }
            aux = aux->siguienteNodo;

        } return NULL;

    }

    void Insertar(int id, int precio, std::string nombre, std::string categoria, std::string src){

        if(vacio()){
            Iniciocate = Fincate = new Nodocategorias(categoria);
            Iniciocate->Barcos->insertarAlFinal(id,precio,nombre,categoria,src,false);
            return;
        } else {
            if(buscar(categoria)==false){
                Nodocategorias* Nuevo = new Nodocategorias(categoria);
                Nuevo->Barcos->insertarAlFinal(id,precio,nombre,categoria,src,false);
                Fincate->siguienteNodo = Nuevo;
                Nuevo->anteriorNodo = Fincate;
                Fincate = Nuevo;
                return;
            } else {
            Nodocategorias* tmp = obtener(categoria);
            tmp->Barcos->insertarAlFinal(id,precio,nombre,categoria,src,false);
            return;
            }


        }
    }
    void imprimir(){
        Nodocategorias* aux = Iniciocate;
        while(aux!=NULL){

            std::cout << "Categoria:" << aux->categoria << " ";

            cout<<endl;
            aux->Barcos->sortListabarquito();
            aux->Barcos->desplegarLista();

            aux = aux->siguienteNodo;
        }
    }
};
