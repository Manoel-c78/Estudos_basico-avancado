import java.util.Scanner;

public class Switch_com_break {
    public static void main (String [] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite um número de 1 a 3: ");
        int num = scanner.nextInt();

        switch (num){
            case 1:
                System.out.println("Gato");
                break;
            case 2:
                System.out.println("Cachorro");
                break;
            case 3:
                System.out.println("Pássaro");
                break;
        }
        System.out.println(num);
    }
}
