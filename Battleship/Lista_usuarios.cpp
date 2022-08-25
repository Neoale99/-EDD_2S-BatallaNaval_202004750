
#include <iostream>
#include "sha256.h"
#include "Lista_usuariosh.h"
#include "Lista_categoriash.h"
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
void Ordenarascendente(){
    nodo* actual = new nodo();
    nodo* temp = new nodo();
    string tmpusuario,tmpcontra;
    int tmpedad, tmpmonedas;

    if(primero!=NULL){
        actual = primero;
        temp = actual->siguiente;
        while(temp!=primero){
            if(actual->edad > temp->edad){
                    cout<< actual->edad <<" : " <<temp->edad;
                tmpusuario = actual->nombre;
                tmpcontra = actual->contra;
                tmpmonedas = actual->monedas;
                tmpedad = actual->edad;

                actual->nombre = temp->nombre;
                actual->contra = temp->contra;
                actual->monedas = temp->monedas;
                actual->edad = temp->edad;

                temp->nombre = tmpusuario;
                temp->contra = tmpcontra;
                temp->monedas = tmpmonedas;
                temp->edad = tmpedad;
            }
            temp = temp->siguiente;

        }
        actual = actual->siguiente;
    } else {
        cout<<"Lista vacia"<<endl;
    }

}
string cifrar(string contrasena){
    return SHA256::cifrar(contrasena);
}
