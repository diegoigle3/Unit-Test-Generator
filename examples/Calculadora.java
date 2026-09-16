public class Calculadora {

    public float sumar(int a, int b) {
        return a + b;
    }

    public float restar(int a, int b) {
        return a - b;
    }
    public float multiplicar(int a, int b) {
        return a * b;
    }
    public float dividir(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("No se puede dividir por cero");
        }
        return a / b;
    }

    private void registrarOperacion(String operacion) {//parser should ignore this method 
        System.out.println("Operación realizada: " + operacion);
    }
}