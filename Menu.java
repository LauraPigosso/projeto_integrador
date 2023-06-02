package com.senai.sp;

import java.util.Scanner;

public class Menu {
    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        String answer = "S";
        int opcao = 0;

        while (true){
            System.out.println("Menu");
            System.out.println("1 - Abrir");
            System.out.println("2 - Criar");
            System.out.println("3 - Alterar");
            System.out.println("4 - Sair");
            System.out.println("Digite a opção desejada:");
            opcao = sc.nextInt();
            switch (opcao) {
                case 1 -> {
                    ExcelReader er = new ExcelReader();
                    er.lerExcel();
                }
                case 2 -> {
                    ExcelWriter ew = new ExcelWriter();
                    ew.criarExcel();
                }
                case 3 -> {
                    ExcelUpdater eu = new ExcelUpdater();
                    eu.atualizarExcel();
                }
                case 4 -> {
                    System.out.println("Deseja finalizar o programa? S ou N");
                    answer = sc.next().toLowerCase();
                }
                default -> System.out.println("Opção inválida!");
            }
            if(answer.equals("s")){
                break;
            }
        }


    }

    public static void exibirMenu() {
        System.out.println("===== MENU =====");
        System.out.println("1 - Criar");
        System.out.println("2 - Abrir");
        System.out.println("3 - Alterar");
        System.out.println("4 - Sair");
    }
}
