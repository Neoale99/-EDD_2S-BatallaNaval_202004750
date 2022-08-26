
#include <cstdlib>
#include <iostream>
#include "Lista_usuariosh.h"
#include "Lista_categoriash.h"
#include "json/json.h"
#include <fstream>
#include "Listabarquito.h"
#include "Lista_categoriash.h"
#include "colah.h"
using namespace std;

void menu();
void carga();
void registrar();
void login();
void reportes();
void sesion_iniciada(string);
void eliminarcuenta(string usuario);
void tutorial();
void tienda(string usuario);
void movimientos();
void modos_de_juego();
Lista_categoria* Articulos = new Lista_categoria();
int anchot,altot;
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
        string url;
        int monedas,edad;
        string tmpstr,usuario,contrasena;
        size_t position;
        string rep = "\"", y = "";

        cout << "Ingrese la ruta del archivo a leer"<<endl;
        cin >> url;
        ifstream ifs(url);
        Json::Reader reader;
        Json::Value obj;
        reader.parse(ifs, obj);
        const Json::Value& usuarios = obj["usuarios"];
        for (int i = 0; i < usuarios.size(); i++){
               usuario = usuarios[i]["nick"].asString();
                tmpstr = usuarios[i]["edad"].asString();
                while ((position = tmpstr.find(rep)) != std::string::npos) {
                tmpstr.replace(position, 1, y);
                }
                edad = stoi(tmpstr);
                tmpstr = usuarios[i]["monedas"].asString();
                while ((position = tmpstr.find(rep)) != std::string::npos) {
                tmpstr.replace(position, 1, y);
                }
                monedas = stoi(tmpstr);
                contrasena = usuarios[i]["password"].asCString();


    insertarmasivo(usuario,contrasena,monedas,edad);
    }

        string categoria,nombre,src;
        int id, precio;
        const Json::Value&  articulos = obj["articulos"];
            for (int i = 0; i < articulos.size(); i++){
                   categoria = articulos[i]["categoria"].asString();
                    tmpstr = articulos[i]["id"].asString();
                    while ((position = tmpstr.find(rep)) != std::string::npos) {
                    tmpstr.replace(position, 1, y);
                    }
                    id = stoi(tmpstr);
                    tmpstr = articulos[i]["precio"].asString();
                    while ((position = tmpstr.find(rep)) != std::string::npos) {
                    tmpstr.replace(position, 1, y);
                    }
                    precio = stoi(tmpstr);
                    src = articulos[i]["src"].asCString();
                    nombre = articulos[i]["nombre"].asCString();
                    Articulos->Insertar(id,precio,nombre,categoria,src );
      }
        int  posx, posy;
        const Json::Value& ancho = obj["tutorial"].get("ancho","");
        tmpstr = ancho.asString();
            while ((position = tmpstr.find(rep)) != std::string::npos) {
            tmpstr.replace(position, 1, y);
            }
        anchot = stoi(tmpstr);
        const Json::Value& alto = obj["tutorial"].get("alto","");
        tmpstr = alto.asString();
            while ((position = tmpstr.find(rep)) != std::string::npos) {
            tmpstr.replace(position, 1, y);
            }
        altot = stoi(tmpstr);
        const Json::Value& posxy = obj ["tutorial"].get("movimientos","");
        for (int i = 0; i < posxy.size(); i++){
            tmpstr = posxy[i]["x"].asString();
            while ((position = tmpstr.find(rep)) != std::string::npos) {
            tmpstr.replace(position, 1, y);
            }
            posx = stoi(tmpstr);

            tmpstr = posxy[i]["y"].asString();
            while ((position = tmpstr.find(rep)) != std::string::npos) {
            tmpstr.replace(position, 1, y);
            }
            posy = stoi(tmpstr);
           insertarCola(posx,posy);
        }
    cout << "Archivo cargado con exito"<<endl;
    menu();
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

		cout << "\n|========================================|";
		cout << "\n| Seleccione la estructura a visualizar  |";
		cout << "\n|========================================|";
		cout << "\n| 1. Lista doblemente enlazada           |";
		cout << "\n| 2. Lista de listas                     |";
		cout << "\n| 3. Cola de movimientos                 |";
		cout << "\n| 4. Lista de pilas                      |";
		cout << "\n| 5. Usuarios ordenados ascendentemente  |";
		cout << "\n| 6. Articulos ordenados ascendentemente |";
		cout << "\n| 7. Usuarios ordenados descendentemente |";
		cout << "\n| 8. Articulos ordenados descendentemente|";
		cout << "\n| 9. Regresar al menu                    |";
		cout << "\n|========================================|";
		cout << "\n\n Escoja una Opcion: ";

        cin >> opcion;

        switch (opcion) {
            case 1:
                cout << "Generando imagen de la lista doblemente enlazada"<<endl;
                desplegarListaPU();
                system(("Listacircular.png"));
                break;

            case 2:
                cout << "Generando imagen de la lista de listas"<<endl;
                break;
            case 3:
                cout << "Generando imagen de la cola de movimientos"<<endl;
                system(("Cola.png"));
                break;

            case 4:
                cout << "Generando imagen de la lista de pilas"<<endl;
                break;
            case 5:
                cout << "Imprimiendo usuarios ordenados de forma ascendente"<<endl;
                Ordenarascendente();
                imprimir();

                break;

            case 6:
                cout << "Imprimiendo articulos ordenados de forma ascendente en precio"<<endl;
                Articulos->Fincate->Barcos->sortListabarquito();
                Articulos->imprimir();

                break;
            case 7:
                cout<< "Imprimiendo usuarios ordenados de forma descendente";
                Ordenardescendente();
                imprimir();
                break;
            case 8:
                cout << "Imprimiendo articulos ordenados de forma descendente en precio"<<endl;

                break;
            case 9:
                cout<< "Regresando al menú...";
                menu();
                break;

            default:
                cout << "Algo salió mal"<<endl;
                reportes();
        }
    } while (opcion!=9);

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
                desplegarCola(anchot,altot);

                break;

            case 4:
                tienda(usuario);
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
    int opcion;
    cout<<"Bienvenido a la tienda, ingrese la accion que desea realizar"<<endl;
    cout<<"1. Comprar"<<endl;
    cout<<"2. Regresar"<<endl;
    cin >> opcion;
    if( opcion== 1){
        Articulos->imprimir();
        cout<<"Actualmente los articulos no estan en venta, vuelva mas tarde"<<endl;
        sesion_iniciada(usuario);
    } else if(opcion == 2){
        sesion_iniciada(usuario);

    }
}
void movimientos(string usuario){

    cout<< "Ingrese las coordenadas a las que disparar en el siguiente formato (x,y)"<<endl;
}
