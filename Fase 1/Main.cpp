#include <iostream>
#include <cstdlib>
using namespace std;

void menu();
void carga();
void registrar();
void login();
void reportes();
void sesion_iniciada(string);
void editar_info(string);
void eliminar_cuenta(string);
void tutorial();
void tienda();
void movimientos();
int main(){
    cout<< "Iniciando programa"<< endl; 
    menu();
}

void menu(){
        int opcion;
        
     do {

		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n|           °     Menú     °          |";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n| 1. Carga masiva                     |";
		cout << "\n| 2. Registrar usuario                |";
		cout << "\n| 3. Login                            |";
		cout << "\n| 4. Reportes                         |";
		cout << "\n| 5. Salir del juego                  |";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Aquí irá la carga masiva"<<endl;
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
    cout<< "Ingrese su usuario: "<<endl;
    cin >> usuario;
    cout<< "Ingrese su contraseña"<<endl;
    cin >> contra;
    if (usuario == "Neo" && contra == "hola")
    {
        cout<<"Bienvenido " << usuario << " nos da gusto volver a verte "<<endl;
        sesion_iniciada(usuario);
    }
    
}
void registrar(){

    string usuario;
    string contra;
    int edad;       //Meter en un ciclo que valide si no existe un usuario con el mismo nombre
    bool doble_usuario = false;
        cout<< "Ingrese el usuario que usará "<<endl;
        cin >> usuario;
        if (usuario == "Comida")
        {
            cout<< "Nombre de usuario ya existente, pruebe con uno distinto"<<endl;
            registrar();        
        } 
        cout<< "Ingrese la contraseña que usará"<<endl;
        cin >> contra;
        cout<< "Ingrese su edad"<<endl;
        cin >> edad;
    return menu();
}
void reportes(){
        int opcion;
        
     do {

		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n| Seleccione la estructura a visualizar |";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n| 1. Lista doblemente enlazada          |";
		cout << "\n| 2. Lista de listas                    |";
		cout << "\n| 3. Cola de movimientos                |";
		cout << "\n| 4. Lista de pilas                     |";
		cout << "\n| 5. Usuarios ordenados                 |";
		cout << "\n| 6. Articulos ordenados                |";
		cout << "\n| 7. Regresar al menu                   |";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
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

		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n|Bienvenido"<< usuario <<"|";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n| 1. Editar informacion               |";
		cout << "\n| 2. Eliminar cuenta                  |";
		cout << "\n| 3. Tutorial                         |";
		cout << "\n| 4. Ver la tienda                    |";
		cout << "\n| 5. Realizar movimientos             |";
		cout << "\n| 5. Logout                           |";
		cout << "\n|♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣♣|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                editar_info(usuario);
                opcion = 5;
                break;

            case 2:
                eliminar_cuenta(usuario);     
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
void editar_info(string usuario){
                                        //Hacer la busqueda en la lista por el nombre de usuario
    
}
void eliminar_cuenta(string usuario){
                                        //Buscar el nodo en la lista y eliminarlo
    cout<<"¿Desea eliminar permanentemente esta cuenta? [y/n]"<<endl;
    string decision;
    cin >> decision;
    if (decision=="y")
    {
        cout <<"Ya se fue la cuenta paps";
        menu();
    } else if (decision=="n")
    {
        cout<<"Regresemos al menú para evitar una tragedia";
        sesion_iniciada(usuario);
    } else {
        cout<<"Algo malió sal, regresando a la pantalla anterior"<<endl;
        sesion_iniciada(usuario);
    }
    
    
}
void tutorial(){}
void tienda(string usuario){
                                        //Buscar el usuario y en la propiedad tienda mostrar y modificar
}
void movimientos(string usuario){

    cout<< "Ingrese las coordenadas a las que disparar en el siguiente formato (x,y)"<<endl;
}
