

#pragma once
#include <iostream>

struct nodo;
void insertarNodo();
bool buscarNodo(std::string usuario);
bool buscarLogin(std::string usuario, std::string contrasena);
void modificarNodo(std::string usuario);
void eliminarNodo(std::string usuario);
void desplegarListaPU();
void insertarmasivo(std::string usuario,std::string contrasena, int monedas, int edad);
void Ordenarascendente();
void Ordenardescendente();
std::string cifrar(std::string contrasena);
void imprimir();
