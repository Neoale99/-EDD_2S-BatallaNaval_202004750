
#include <cstdlib>
#include <iostream>
#include "Lista_usuariosh.h"

using namespace std;

void menu();
void carga();
void registrar();
void login();
void reportes();
void sesion_iniciada(string);
void eliminarcuenta(string usuario);
void tutorial();
void tienda();
void movimientos();
void modos_de_juego();
int main(){
    cout<< "Iniciando programa"<< endl;
    menu();
}

void menu(){
        int opcion;

     do {

		cout << "\n|=====================================|";
		cout << "\n|                 Menu                |";
		cout << "\n|=====================================|";
		cout << "\n| 1. Carga masiva                     |";
		cout << "\n| 2. Registrar usuario                |";
		cout << "\n| 3. Login                            |";
		cout << "\n| 4. Reportes                         |";
		cout << "\n| 5. Salir del juego                  |";
		cout << "\n|=====================================|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Aqui ira la carga masiva"<<endl;
                carga();
                opcion = 5;
                break;

            case 2:
                registrar();
                opcion = 5;
                break;
            case 3:
                login();
                opcion = 5;
                break;

            case 4:
                reportes();
                opcion = 5;
                break;
            case 5:
                cout<< "Muchas gracias por jugar Battleship";
                break;

            default:
                cout << "Algo salió mal"<<endl;
                menu();
        }
    } while (opcion!=5);

    return;

}

void carga(){

    cout<< "Ingrese la ruta del archivo"<<endl;
    cout<< "Archivo cargado"<<endl;

}
void login(){
    string usuario;
    string contra;
	char con[20];
    cout<< "Ingrese su usuario: "<<endl;
    cin >> usuario;
    cout<< "Ingrese su contrasena"<<endl;
    cin >> con;
    contra = con;
    if(buscarLogin(usuario,cifrar(contra))==true){
     sesion_iniciada(usuario);
    } else{
     cout<<" Usuario o contrasena incorrectos, regresando al menu"<<endl;
     menu();
    }

}
void registrar(){

    insertarNodo();
    return menu();
}
void reportes(){
        int opcion;

     do {

		cout << "\n|=======================================|";
		cout << "\n| Seleccione la estructura a visualizar |";
		cout << "\n|=======================================|";
		cout << "\n| 1. Lista doblemente enlazada          |";
		cout << "\n| 2. Lista de listas                    |";
		cout << "\n| 3. Cola de movimientos                |";
		cout << "\n| 4. Lista de pilas                     |";
		cout << "\n| 5. Usuarios ordenados                 |";
		cout << "\n| 6. Articulos ordenados                |";
		cout << "\n| 7. Regresar al menu                   |";
		cout << "\n|=======================================|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Generando imagen de la lista doblemente enlazada"<<endl;

                opcion = 5;
                break;

            case 2:
                cout << "Generando imagen de la lista de listas"<<endl;
                opcion = 5;
                break;
            case 3:
                cout << "Generando imagen de la cola de movimientos"<<endl;
                break;

            case 4:
                cout << "Generando imagen de la lista de pilas"<<endl;
                break;
            case 5:
                cout << "Imprimiendo usuarios ordenados de forma descendente"<<endl;
                break;

            case 6:
                cout << "Imprimiendo articulos ordenados de forma ascendente en precio"<<endl;
                break;
            case 7:
                cout<< "Regresando al menú...";
                menu();
                break;

            default:
                cout << "Algo salió mal"<<endl;
                reportes();
        }
    } while (opcion!=7);

    return;
}
void sesion_iniciada(string usuario){
        int opcion;

     do {

		cout << "\n|=====================================|";
		cout << "\n       Bienvenido "<< usuario ;
		cout << "\n|=====================================|";
		cout << "\n| 1. Editar informacion               |";
		cout << "\n| 2. Eliminar cuenta                  |";
		cout << "\n| 3. Tutorial                         |";
		cout << "\n| 4. Ver la tienda                    |";
		cout << "\n| 5. Realizar movimientos             |";
		cout << "\n| 6. Modos de juego                   |";
		cout << "\n| 7. Logout                           |";
		cout << "\n|=====================================|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                modificarNodo(usuario);
                opcion = 7;
                break;

            case 2:
                eliminarcuenta(usuario);
                opcion = 7;
                break;
            case 3:
                login();
                opcion = 7;
                break;

            case 4:
                reportes();
                opcion = 7;
                break;
            case 5:
                cout<< "Muchas gracias por jugar Battleship";
                opcion = 7;
                break;
            case 6:
                cout<<"El modo de juego 1 jugador se encuentra en desarrollo";
                opcion = 7;
                break;
            case 7:
                cout<< "Muchas gracias por jugar Battleship";
                menu();
                opcion = 7;
                break;

            default:
                cout << "Algo salió mal"<<endl;
                menu();
        }
    } while (opcion!=7);

    return;


}



void tutorial(){
}
void eliminarcuenta(string usuario){
    string confirmacion;
    cout << "Desea realmente eliminar su cuenta? [si/no]"<<endl;
    cin >> confirmacion;
    if (confirmacion == "si"){
        eliminarNodo(usuario);
        menu();
    }  else if (confirmacion == "no") {
        cout << "Cuenta no eliminada, regresando al menu"<<endl;
        sesion_iniciada(usuario);
    }   else {
        cout << "Algo salió mal, reintentado"<<endl;
        eliminarcuenta(usuario);
    }
}
void tienda(string usuario){
                                        //Buscar el usuario y en la propiedad tienda mostrar y modificar
}
void movimientos(string usuario){

    cout<< "Ingrese las coordenadas a las que disparar en el siguiente formato (x,y)"<<endl;
}
