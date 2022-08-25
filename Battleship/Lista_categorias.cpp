

#include "Lista_categoriash.h"

using namespace std;

struct nodocategorias{
	string  categoria;
	nodocategorias* siguiente;
} *primeroc, *ultimoc;


//void insertarNodoC(std::string categoria, int id, int precio, std::string nombre, std::string src){
//	nodocategorias* nuevo = new nodocategorias();
//	 nuevo->categoria = categoria;
//    bool condicion = buscarNodoC(categoria);
//	if(primeroc == NULL){
//		primeroc = nuevo;
//        primeroc->siguiente = NULL;
//		ultimoc = nuevo;
//	}else{
//		ultimoc->siguiente = nuevo;
//		nuevo->siguiente = NULL;
//		ultimoc = nuevo;
//	}
//
//}
void modificarNodo(){ //Uso futuro para modificar el booleano de comprado
	nodocategorias* actual = new nodocategorias();
	actual = primeroc;
	bool encontrado = false;
	string nodoBuscado = "";
	cout << " Ingrese el dato del nodo a Buscar para Modificar: ";
	cin >> nodoBuscado;
	if(primeroc != NULL){

		while(actual != NULL && encontrado != true){

			if(actual->categoria == nodoBuscado){
				cout << "\n Nodo con el categoria " << nodoBuscado << " Encontrado";
				cout << "\n Ingrese el Nuevo categoria para este Nodo: ";
				cin >> actual->categoria;
				encontrado = true;
			}

			actual = actual->siguiente;
		}
		if(!encontrado){
			cout << "\n Nodo No Encontrado\n\n";
		}
	}else{
		cout  << "\n La Lista se Encuentra Vacia\n\n";
	}
}
bool buscarNodoC(string categoria){
	nodocategorias* actual = new nodocategorias();
	actual = primeroc;
	bool encontrado = false;
	string nodoBuscado = categoria;
	if(primeroc!=NULL){

		do{

			if(actual->categoria==nodoBuscado){

				encontrado = true;
				return true;
			}

			actual = actual->siguiente;
		}while(actual!=primeroc && encontrado != true);

		if(!encontrado){

			return false;
		}

	}else{
    return false;
	}

}
void desplegarLista(){
	nodocategorias* actual = new nodocategorias();
	actual = primeroc;
	if(primeroc != NULL){

		while(actual != NULL){
			cout << " " << actual->categoria  << endl;
			actual = actual->siguiente;
		}

	}else{
		cout  << "\n La Lista se Encuentra Vacia\n\n";
	}
}
