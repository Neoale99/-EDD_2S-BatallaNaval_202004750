#include <iostream>
#include <string>
#include <windows.h>
#include <fstream>
#include <sstream>
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
    string dot ="digraph G{ bgcolor = LightSalmon; \n";
    dot+="node[shape=box3d, style=filled,color = SlateBlue ,fillcolor = azure];\n";
	string tuto = "Tutorial\n \tTablero\n";
	tuto += "-----------------------------------------\n";
	tuto += "ancho: " + to_string(x)+"\n";
	tuto += "alto: " + to_string(y)+"\n";
	tuto += "-----------------------------------------\n";
	int i = 1;
	if (primerocola != NULL) {
		while (actual != NULL) {
			if (actual->siguiente == NULL)
			{

                dot+= "nodo"+ to_string(i)+"[label=\" X:" + to_string(actual->posx) + " \\n Y:" + to_string(actual->posy) +"\"]\n";
				tuto += "(" + to_string(actual->posx) + "," + to_string(actual->posy) + ")";
				actual = actual->siguiente;
                i+=1;
			}
			else {

                dot+= "nodo"+ to_string(i)+"[label=\" X:" + to_string(actual->posx) + " \\n Y:" + to_string(actual->posy) +"\"]\n";
				tuto += "(" + to_string(actual->posx) + "," + to_string(actual->posy) + ") ->";
				actual = actual->siguiente;
				i+=1;
				}
		}
	}
	else {
		cout << endl << " La cola se encuentra Vacia " << endl << endl;
	}
	for(int j = 1;j<i;j++){


        if(j+1==i){
            dot+="nodo"+to_string(j);

        } else{
             dot+="nodo"+to_string(j)+"->";
        }


	}
	dot+="\n rankdir=UD; \n}";
	cout <<tuto<<endl;;
    ofstream file;
    file.open("Cola.dot");
    file << dot;
    file.close();


    system(("dot -Tpng Cola.dot -o  Cola.png"));
	//dequeue();
}


