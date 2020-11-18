public class FibonacciNumbers {
    public int fib(int N) {
        return (int) ((1 / sqrt5()) * (Math.pow((1 + sqrt5()) / 2, N) - Math.pow((1 - sqrt5()) / 2, N)));
    }

    private double sqrt5() {
        return Math.sqrt(5);
    }
}
