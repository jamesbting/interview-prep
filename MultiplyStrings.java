public class MultiplyStrings {

    public String multiply(String num1, String num2) {
        if (num1.equals("0") || num2.equals("0"))
            return "0";
        if (num1.equals("1"))
            return num2;
        if (num2.equals("1"))
            return num1;

        int power = 0;
        String product = "0";
        for (int j = num2.length() - 1; j >= 0; j--) {
            int m = num2.charAt(j) - '0';
            int sum = 0;
            for (int i = 0; i < num1.length(); i++) {
                int n = num1.charAt(i) - '0';
                sum = (sum * 10) + (n * m);
            }
            sum *= Math.pow(10, power);
            power++;
            product = add("" + sum, product);
        }

        return product;
    }

    private String add(String num1, String num2) {
        if (num2.equals("0"))
            return num1;
        int i = 0;
        int j = 0;
        if (num1.length() < num2.length())
            i = -1 * (num2.length() - num1.length());
        if (num1.length() > num2.length())
            j = -1 * (num1.length() - num2.length());
        int sum = 0;
        while (i < num1.length() && j < num2.length()) {
            int n = i >= 0 ? num1.charAt(i) - '0' : 0;
            int m = j >= 0 ? num2.charAt(j) - '0' : 0;
            int carry = (n + m) / 10;
            int rest = (n + m) / 10;

            sum = (sum * 10) + (n + m);
            i++;
            j++;
        }

        return "" + sum;
    }

}
