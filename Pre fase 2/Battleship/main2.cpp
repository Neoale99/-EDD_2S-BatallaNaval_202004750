
#include <iostream>
#include "Btree.h"
using namespace std;

int main2(){
    BTree* t = new BTree(2); //Insertarlos manualmente

    //t->insert("Carlos", nodo_usuario);
    t->insert("Folagor", insertarNodo("Folagor", "alfal475", 700, 29));
    t->insert("Planton", insertarNodo("Planton", "cam78dad", 50, 20));
    t->insert("Pikachu", insertarNodo("Pikachu", "beliz5a4", 59, 18));
    t->insert("Naruto", insertarNodo("Naruto", "jfagaga16a", 80, 19));
    t->insert("Goku", insertarNodo("Goku", "agga516r", 56, 20));
    t->traverse();
    //t->search("Pikachu");

    t->DrawBTree();
    return 0;
}
