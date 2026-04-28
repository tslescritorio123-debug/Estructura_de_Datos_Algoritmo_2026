#include <iostream>
using namespace std;
int main() {
    float num1, num2, resultado;
    char operador;

    cout << "----- CALCULADORA -----" << endl;
    
    cout << "Ingrese el primer número: ";
    cin >> num1;

    cout << "Ingrese el operador (+, -, *, /): ";
    cin >> operador;

    cout << "Ingrese el segundo número: ";
    cin >> num2;

    switch (operador) {
        case '+':
            resultado = num1 + num2;
            cout << "Resultado: " << num1 << " + " << num2 << " = " << resultado << endl;
            break;
        case '-':
            resultado = num1 - num2;
            cout << "Resultado: " << num1 << " - " << num2 << " = " << resultado << endl;
            break;
        case '*':
            resultado = num1 * num2;
            cout << "Resultado: " << num1 << " * " << num2 << " = " << resultado << endl;
            break;
        case '/':
            // Validación
            if (num2 != 0) {
                resultado = num1 / num2;
                cout << "Resultado: " << num1 << " / " << num2 << " = " << resultado << endl;
            } else {
                cout << "Error: No se puede dividir entre cero." << endl;
            }
            break;
        default:
            cout << "Operador no válido. Use +, -, * o /." << endl;
            break;
    }

    return 0;
}
// Actualización del informe - Gabriela Díaz