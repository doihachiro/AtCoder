import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        String[] word = new String[N];

        for (int i = 0; i < N; i++) {
            word[i] = sc.next();
        }

        for (int i = 0; i < N; i++) {
            if (word[i].equals("and") || word[i].equals("not") || word[i].equals("that") || word[i].equals("the") || word[i].equals("you")) {
                System.out.println("Yes");
                return;
            }
        }
        System.out.println("No");
    }
}