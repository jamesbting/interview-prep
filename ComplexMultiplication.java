import java.lang.*;

public class ComplexMultiplication {
    public String complexNumberMultiply(String A, String B) {
        int[] aArr = parseComplex(A);
        int[] bArr = parseComplex(B);
        StringBuilder sb = new StringBuilder();
        int a = aArr[0];
        int b = aArr[1];

        int c = bArr[0];
        int d = bArr[1];
        sb.append((a * c) - (b * d));
        sb.append("+");
        sb.append(((b * c) + (a * d)) + "i");
        return sb.toString();
    }

    private int[] parseComplex(String num) {
        String[] split = num.split("\\+");
        int[] res = new int[2];
        res[0] = Integer.parseInt(split[0]);
        res[1] = Integer.parseInt(split[1].substring(0, split[1].length() - 1));
        return res;
    }
}
