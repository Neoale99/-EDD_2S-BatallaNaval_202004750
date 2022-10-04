

#pragma once
#include <iostream>

struct nodo;
nodo* insertarNodo(std::string usuario, std::string contrasena, int monedas, int edad);
bool buscarNodo(std::string usuario);
bool buscarLogin(std::string usuario, std::string contrasena);
void modificarNodo(std::string usuario);
void eliminarNodo(std::string usuario);
void desplegarListaPU();
nodo* insertarmasivo(std::string usuario,std::string contrasena, int monedas, int edad);
void Ordenarascendente();
void Ordenardescendente();
std::string cifrar(std::string contrasena);
void imprimir();
std::string mostrarDatos2();