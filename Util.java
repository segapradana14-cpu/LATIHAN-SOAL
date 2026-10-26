import java.util.Locale;
import java.util.Scanner;

public class Util {
    private static final Scanner sc = new Scanner(System.in);

    public static String rupiah(double nilai) {
        return "Rp" + String.format(Locale.US, "%,.0f", nilai).replace(',', '.');
    }

    public static String bacaString(String prompt) {
        System.out.print(prompt);
        return sc.nextLine().trim();
    }

    public static int bacaInt(String prompt) {
        while (true) {
            try {
                return Integer.parseInt(bacaString(prompt));
            } catch (NumberFormatException e) {
                System.out.println("Input harus berupa angka bulat!");
            }
        }
    }

    public static double bacaDouble(String prompt) {
        while (true) {
            try {
                return Double.parseDouble(bacaString(prompt));
            } catch (NumberFormatException e) {
                System.out.println("Input harus berupa angka!");
            }
        }
    }
}
