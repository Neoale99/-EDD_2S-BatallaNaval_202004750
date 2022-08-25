
#include <iostream>
#include "Listabarquito.h"
using namespace std;

int main2(){
    Listabarquito* barquitos = new Listabarquito();
    barquitos->insertarAlFinal(1,1200,"proyecto puto","Legendaria","putoelquelolea",false);
    barquitos->insertarAlFinal(2,2000,"proyecto putisimo","Trasto","desputoelquelolea",false);
    barquitos->insertarAlFinal(1,1200,"proyecto mierda","epico","Holamama",false);
    barquitos->insertarAlFinal(2,2000,"proyecto lptm","Trasto","mequieromatar",false);
    barquitos->desplegarLista();
    return 0;
}
