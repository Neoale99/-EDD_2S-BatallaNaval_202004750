
#pragma once
#include "nodobarquito.h"
#include <iostream>

using namespace std;

class Listabarquito{
	private:
		Nodobarquito* primero;
		Nodobarquito* ultimo;
		int largo;
	public:

		Listabarquito(){
	this->primero = NULL;
	this->ultimo = NULL;
	this->largo = 0;
}
bool estaVacio(){
	return this->primero == NULL;
}

int tamanio(){
	int count = 0;
	if(this->estaVacio()){
		return count;
	}
	Nodobarquito* tmp = new Nodobarquito();
	tmp = this->primero;
	while (tmp != NULL){
		count += 1;
		tmp = tmp->siguienteB;
	}
	return count;
}


void insertarAlFinal(int id, int precio, std::string nombre, std::string categoria, std::string src,bool comprado){
	Nodobarquito* nuevo = new Nodobarquito(id, precio, nombre, categoria, src, comprado);
	Nodobarquito* tmp = new Nodobarquito();


	if(this->estaVacio()){
		this->primero = this->ultimo = nuevo;
	}else{
		tmp = this->ultimo;
		this->ultimo = nuevo;
		tmp->siguienteB = this->ultimo;
	}
	this->largo+=1;

}


void eliminarAlFinal(){
	Nodobarquito* tmp = new Nodobarquito();

	if(this->estaVacio()){
		cout<<"Lista vacia"<<endl;
		return;
	}else if(this->primero == this->ultimo){
		this->primero = this->ultimo = NULL;
	}else{
		tmp = this->primero;
		while(tmp->siguienteB != this->ultimo){
			tmp = tmp->siguienteB;
		}
		tmp->siguienteB = NULL;
	}
}

bool buscarNodo(int id){
	Nodobarquito* tmp = new Nodobarquito();

	if(this->estaVacio()){
		cout<<"La lista no contiene elementos... "<<endl;
		return false;
	}

	tmp = this->primero;
	while(tmp != NULL){
		if(tmp->barquito->id == id){
			cout<<id<<" , encontrado. \n"<<endl;
			return true;
		}
		tmp = tmp->siguienteB;
	}
	cout<<id<<", no encontrado. \n"<<endl;
	return false;
}
Nodobarquito* buscarBarco(int id){
	Nodobarquito* tmp = new Nodobarquito();

	if(this->estaVacio()){

		return NULL;
	}

	tmp = this->primero;
	while(tmp != NULL){
		if(tmp->barquito->id == id){
			return tmp;
		}
		tmp = tmp->siguienteB;
	}

	return NULL;
}


void desplegarLista(){
    int contar;
	if(this->estaVacio()){
		cout<< "La lista se encuentra vacia"<<endl;
		return;
	}
	Nodobarquito* tmp = new Nodobarquito();
	tmp = this->primero;
	while(tmp != NULL){
		tmp->barquito->mostrar();
		contar+=1;
		cout << contar;
		tmp = tmp->siguienteB;
	}
	cout<<"\n"<<endl;
}
void sortListabarquito(){
	Nodobarquito* actual = new Nodobarquito();
	Nodobarquito* temp = new Nodobarquito();
	Nodobarquito* auxiliar = new Nodobarquito();
	if(!this->estaVacio()){
		actual = this->primero;

		while(actual->siguienteB != NULL){
            cout << "Aqui si llego" <<endl;
			auxiliar = actual->siguienteB;
			while(auxiliar != primero){
				if(auxiliar->barquito->precio < actual->barquito->precio){

                    cout << auxiliar->barquito->precio <<" : " << actual->barquito->precio <<endl;
                    temp->barquito = actual->barquito;
                    actual->barquito = auxiliar->barquito;
                    auxiliar->barquito = temp->barquito;

				}
				auxiliar = auxiliar->siguienteB;
			}

			actual = actual->siguienteB;
		}
	}else{
		cout<<"No hay elementos que ordenar"<<endl;
	}
}
};






