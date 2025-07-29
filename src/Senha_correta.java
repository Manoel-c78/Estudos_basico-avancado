import java.util.Scanner;

public class Senha_correta {
    public static void main(String [] args){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite a senha: ");
        int senha = scanner.nextInt();

        do {
            System.out.println("Senha incorreta, tente novamente: ");
            senha = scanner.nextInt();
        } while (senha != 1234);
    }
}
