

#pragma once
#include <iostream>

struct nodo;
void insertarNodo();
bool buscarNodo(std::string usuario);
bool buscarLogin(std::string usuario, std::string contrasena);
void modificarNodo(std::string usuario);
void eliminarNodo(std::string usuario);
void desplegarListaPU();
std::string cifrar(std::string contrasena);
