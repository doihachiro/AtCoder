import java.util.*;

public class Main {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int  n = scan.nextInt();

        for (int i = 1; i <= n; i++) {
            int x = scan.nextInt();

            if (x % 2 == 0){
                System.out.print(x+" ");
            }
        }
    }
}