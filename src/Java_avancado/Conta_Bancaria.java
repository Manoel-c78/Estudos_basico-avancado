package Java_avancado;

import java.util.Scanner;

public class Conta_Bancaria {
    String nomeCliente;
    float saldo;

    public Conta_Bancaria(String nomeCliente, float saldo){
        this.nomeCliente = nomeCliente;
        this.saldo = saldo;
    }

    public void depositar(){
        Scanner scanner = new Scanner(System.in);
        System.out.println("Quanto você deseja depositar?");
        float deposito = scanner.nextFloat();

        saldo = saldo + deposito;
        System.out.printf("Depósito de R$ %,.2f realizado com sucesso! Novo saldo: R$ %,.2f%n", deposito, saldo);
    }

    public void sacar(){
        Scanner scanner = new Scanner(System.in);

        System.out.println("Quanto você deseja sacar?");
        float saque = scanner.nextFloat();

        if(saque > saldo){
            System.out.println("Valor do saque maior do que o saldo disponível. Digite um valor menor ou igual ao saldo!");
        } else {
            saldo = saldo - saque;
            System.out.printf("Saque de R$ %,.2f realizado com sucesso! Novo saldo: R$ %,.2f%n", saque, saldo);
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Digite seu nome: ");
        String nome = scanner.nextLine();

        System.out.print("Digite o saldo inicial: ");
        float saldoInicial = scanner.nextFloat();

        Conta_Bancaria conta = new Conta_Bancaria(nome, saldoInicial);

        int opcao = 0;
        do {
            System.out.println("\n--- MENU ---");
            System.out.println("1. Depositar");
            System.out.println("2. Sacar");
            System.out.println("3. Sair");
            System.out.print("Escolha uma opção: ");
            opcao = scanner.nextInt();

            switch(opcao) {
                case 1:
                    conta.depositar();
                    break;
                case 2:
                    conta.sacar();
                    break;
                case 3:
                    System.out.println("Encerrando...");
                    break;
                default:
                    System.out.println("Opção inválida!");
            }
        } while(opcao != 3);

        scanner.close();
    }
}
