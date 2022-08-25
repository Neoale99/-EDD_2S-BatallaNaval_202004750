#include <iostream>
#include <string>
using namespace::std;

struct nodo {
	int posx;
	int posy;
	nodo* siguiente;
} *primerocola, * ultimocola;

void dequeue() {
	nodo* actual = new nodo();
	nodo* tmp = new nodo();
	actual = primerocola;
	while (actual->siguiente != NULL)
	{
		tmp = actual->siguiente;
		actual->siguiente = tmp->siguiente;
		delete(tmp);
	}
	actual->siguiente = NULL;


}
void insertarCola(int x, int y) {
	nodo* nuevo = new nodo();
	nuevo->posx = x;
	nuevo->posy = y;

	if (primerocola == NULL) {
		primerocola = nuevo;
		primerocola->siguiente = NULL;
		ultimocola = primerocola;
	}
	else {
		ultimocola->siguiente = nuevo;
		nuevo->siguiente = NULL;
		ultimocola = nuevo;
	}

}





void desplegarCola(int x, int y) {
	nodo* actual = new nodo();
	actual = primerocola;

	string tuto = "Tutorial\n \tTablero\n";
	tuto += "-----------------------------------------\n";
	tuto += "ancho: " + to_string(x)+"\n";
	tuto += "alto: " + to_string(y)+"\n";
	tuto += "-----------------------------------------\n";
	int i;
	if (primerocola != NULL) {
		while (actual != NULL) {
			if (actual->siguiente == NULL)
			{
				tuto += "(" + to_string(actual->posx) + "," + to_string(actual->posy) + ")";
				actual = actual->siguiente;
			}
			else {
				tuto += "(" + to_string(actual->posx) + "," + to_string(actual->posy) + ") ->";
				actual = actual->siguiente;
				}
		}
	}
	else {
		cout << endl << " La cola se encuentra Vacia " << endl << endl;
	}
	cout <<tuto;
	//dequeue();
}

