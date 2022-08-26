
#include <iostream>
#include <windows.h>
#include <fstream>
#include <sstream>
#include <string>
#include "sha256.h"
#include "Lista_usuariosh.h"
#include "Lista_categoriash.h"
using namespace::std;
struct nodo{
	int edad;
    string nombre;
    int monedas;
    string contra;

	nodo* siguiente;
	nodo* atras;
} *primero, *ultimo;

void insertarNodo(){
	char con[20];
	string tmp;
	bool condicion;
	nodo* nuevo = new nodo();
    cout << "Ingrese su usuario ";
    cin >> tmp;

    condicion = buscarNodo(tmp);
    if (condicion!=1){
    nuevo->nombre = tmp;
    cout << "Ingrese su edad: ";
	cin >> nuevo->edad;
    nuevo->monedas = 0;
    cout << "Ingrese su contrasena ";
	cin >> con;
	tmp = con;
	nuevo->contra = SHA256::cifrar(tmp);
	if(primero==NULL){
		primero = nuevo;
		ultimo = nuevo;
		primero->siguiente = primero;
		primero->atras = ultimo;
	}else{
		ultimo->siguiente = nuevo;
		nuevo->atras = ultimo;
		nuevo->siguiente = primero;
		ultimo = nuevo;
		primero->atras = ultimo;
	}
	cout << "\n Usuario creado\n\n";
    } else {
        cout << "Usuario ya existente, ustilice uno distinto"<< endl;
        insertarNodo();
    }
}

void insertarmasivo(string usuario, string contrasena, int monedas, int edad){
    bool condicion;
    nodo* nuevo = new nodo();
    condicion = buscarNodo(usuario);
    if (condicion!=1){
    nuevo->nombre = usuario;
    nuevo->edad = edad;
    nuevo->monedas = monedas;
	nuevo->contra = SHA256::cifrar(contrasena);

	if(primero==NULL){
		primero = nuevo;
		ultimo = nuevo;
		primero->siguiente = primero;
		primero->atras = ultimo;
	}else{
		ultimo->siguiente = nuevo;
		nuevo->atras = ultimo;
		nuevo->siguiente = primero;
		ultimo = nuevo;
		primero->atras = ultimo;
	}
	cout << "\n Usuario creado\n\n";
    } else {
        cout << "Usuario ya existente, ustilice uno distinto"<< endl;
        insertarNodo();
    }



    }

bool buscarNodo(string usuario){
	nodo* actual = new nodo();
	actual = primero;
	bool encontrado = false;
	string nodoBuscado = usuario;
	if(primero!=NULL){

		do{

			if(actual->nombre==nodoBuscado){

				encontrado = true;
				return true;
			}

			actual = actual->siguiente;
		}while(actual!=primero && encontrado != true);

		if(!encontrado){

			return false;
		}

	}else{
    return false;
	}

}

bool buscarLogin(std::string usuario, std::string contrasena){ //Buscar porque estos son los unicos que me pide con std::string
    nodo* actual = new nodo();
	actual = primero;
	bool encontrado = false;
	string nodoBuscado = usuario;
	string contraval = contrasena; //validación de la contraseña
		do{

			if(actual->nombre==nodoBuscado&&actual->contra==contraval){
				encontrado = true;

				return true;
			}

			actual = actual->siguiente;
		}while(actual!=primero && encontrado != true);

		if(!encontrado){
			cout << "\n Usuario no encontrado\n\n";
			return false;
		}

	else{
		cout << "\n No hay usuarios registrados\n\n";
	}
	return false;
}

void modificarNodo(string usuario){ //Aquí debo pasar por parámetro el usuario para buscarlo y sacar su info
	nodo* actual = new nodo();
	actual = primero;
	bool encontrado = false;
	string tmp ="";
	char con[20];
    string nodo_buscado = usuario;
	if(primero!=NULL){
		do{

			if(actual->nombre==nodo_buscado){
				cout << "\n Usuario ( " << nodo_buscado << " ) Encontrado";

				cout << "\n Ingrese su nueva edad: ";
				cin >> actual->edad;
				cout << "\n Ingrese su nuevo usuario: \n\n";
                cin >> actual ->nombre;
				cout << "\n Ingrese su nueva contraseña: ";
                cin >> con;
                tmp = con;
                actual->contra = SHA256::cifrar(tmp);
				encontrado = true;
			}

			actual = actual->siguiente;
		}while(actual!=primero && encontrado != true);

		if(!encontrado){
			cout << "\n Usuario no encontrado, algo salió muy mal\n\n";
		}

	}else{
		cout << "\n Si este mensaje sale me mato\n\n";
	}
}

void eliminarNodo(string usuario){ //Pasar por parámetro tambien y luego eliminar
	nodo* actual = new nodo();
	actual = primero;
	nodo* anterior = new nodo();
	anterior = NULL;
	bool encontrado = false;
	string nodoBuscado = usuario;
	if(primero!=NULL){
		do{

			if(actual->nombre==nodoBuscado){
				if(actual==primero){ //Lo situamos al inicio de la lista
					primero = primero->siguiente; //Nos movemos una posición hacia adelante
					primero->atras = ultimo; //Ponemos la posición final de primero en el ultimo nodo
					ultimo->siguiente = primero; //Encadenamos la lista circular, despues del fin, saltamos al inicio
				}else if(actual==ultimo){ //Si nuestro puntero llega al final de la lista
					ultimo = anterior; //Pasamos el ultimo a uno atrás
					ultimo->siguiente = primero; //El "Final" nos llevará al inicio
					primero->atras = ultimo; //Regresamos a su posición el final
				}else{
					anterior->siguiente = actual->siguiente; //El anterior pasa a ser el siguiente
					actual->siguiente->atras = anterior; //Cambiamos el actual hacia "anterior"
				}

				cout << "\n Cuenta eliminada \n\n";
				encontrado = true;
			}

			anterior = actual;
			actual = actual->siguiente;
		}while(actual!=primero && encontrado != true);

		if(!encontrado){
			cout << "Este es otro mensaje que no debería salir nunca, si sale debería empezar a llorar";
		}

	}else{
		cout <<"Algo salió mal, si estas viendo este mensaje deberías empezar a llorar";
	}
}

void desplegarListaPU(){
    int i = 1;
    int tmpedad,tmpmon;
    string dot ="digraph G{ bgcolor = LightSalmon; \n";
    dot+="node[shape=box3d, style=filled,color = SlateBlue ,fillcolor = azure];\n";
	nodo* actual = new nodo();
	actual = primero;
	if(primero!=NULL){
		do{
            tmpedad = actual->edad;
            tmpmon = actual->monedas;
            dot+= "nodo" + to_string(i)+"[label=\" Nombre: " + actual->nombre + " \\n contrasena: " + actual->contra + "\\n Edad: "+ to_string(tmpedad) +"\\n Monedas: "+to_string(tmpmon)+"\"]\n";
			//cout << "\n Nombre: " << actual->nombre;
			//cout << "\n Edad: " << actual->edad;
			//cout << "\n Contraseña: " << actual->contra;
			//cout << "\n Monedas: " << actual->monedas<<endl;
			actual = actual->siguiente;
			i+=1;
		}while(actual!=primero);

	}else{
		cout << "\n La lista se Encuentra Vacia\n\n";
	}
	for(int j = 1;j<i;j++){


        if(j+1==i){
            dot+="nodo"+to_string(j)+"->nodo"+to_string(1);

        } else{
             dot+="nodo"+to_string(j)+"->";
        }


	}
	dot+="\n rankdir=UD; \n}";
    ofstream file;
    file.open("Listacircular.dot");
    file << dot;
    file.close();


    system(("dot -Tpng Listacircular.dot -o  Listacircular.png"));
}
void Ordenarascendente(){
    nodo* actual = new nodo();
    nodo* temp = new nodo();
    nodo* auxiliar = new nodo();
    int i = 0;
    if(primero!=NULL){
        actual = primero;
        while(actual->siguiente!=primero){
            auxiliar = actual->siguiente;
            while (auxiliar!=primero){ // No poner NULL que se encicla al infinito, luego de revisar varias veces alfin encontré que era por eso
                if(auxiliar->edad < actual->edad){
                    temp->edad = actual->edad;
                    temp->nombre = actual->nombre;
                    temp->monedas = actual->monedas;
                    temp->contra=actual->contra;

                    actual->edad = auxiliar->edad;
                    actual->nombre = auxiliar->nombre;
                    actual->monedas = auxiliar->monedas;
                    actual->contra = auxiliar->contra;

                    auxiliar->edad = temp->edad;
                    auxiliar->nombre = temp->nombre;
                    auxiliar->contra = temp->contra;
                    auxiliar->monedas = temp->monedas;
                    i+=1;


                }
                int edd;
                edd = actual->edad;
                cout << i<< " : "<<edd  ;
                auxiliar = auxiliar->siguiente;
            }
            actual = actual->siguiente;

        }

    } else {
        cout<<"Lista vacia"<<endl;
    }

}
void Ordenardescendente(){
    nodo* actual = new nodo();
    nodo* temp = new nodo();
    nodo* auxiliar = new nodo();
    int i = 0;
    if(primero!=NULL){
        actual = primero;
        while(actual->siguiente!=primero){
            auxiliar = actual->siguiente;
            while (auxiliar!=primero){ // No poner NULL que se encicla al infinito, luego de revisar varias veces alfin encontré que era por eso
                if(auxiliar->edad > actual->edad){
                    temp->edad = actual->edad;
                    temp->nombre = actual->nombre;
                    temp->monedas = actual->monedas;
                    temp->contra=actual->contra;

                    actual->edad = auxiliar->edad;
                    actual->nombre = auxiliar->nombre;
                    actual->monedas = auxiliar->monedas;
                    actual->contra = auxiliar->contra;

                    auxiliar->edad = temp->edad;
                    auxiliar->nombre = temp->nombre;
                    auxiliar->contra = temp->contra;
                    auxiliar->monedas = temp->monedas;
                    i+=1;


                }

                auxiliar = auxiliar->siguiente;
            }
            actual = actual->siguiente;

        }

    } else {
        cout<<"Lista vacia"<<endl;
    }

}
void imprimir(){
	nodo* actual = new nodo();
	actual = primero;
	if(primero!=NULL){
		do{
			cout << "\n Nombre: " << actual->nombre;
			cout << "\n Edad: " << actual->edad;
			cout << "\n Contraseña: " << actual->contra;
			cout << "\n Monedas: " << actual->monedas<<endl;
			actual = actual->siguiente;
		}while(actual!=primero);

	}else{
		cout << "\n La lista se Encuentra Vacia\n\n";
	}


}
string cifrar(string contrasena){
    return SHA256::cifrar(contrasena);
}
