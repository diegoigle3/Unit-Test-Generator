public class Calculadora {

    public float add(int a, int b) {
        return a + b;
    }

    public float subtract(int a, int b) {
        return a - b;
    }
    public float multiply(int a, int b) {
        return a * b;
    }
    public float divide(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("Cannot divide by zero");
        }
        return a / b;
    }

    private void logOperation(String operation) {// parser should ignore this method 
        System.out.println("Operation performed: " + operation);
    }
}