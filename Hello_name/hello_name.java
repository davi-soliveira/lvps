//importação de ferramentas
import java.io.IOException;
import java.util.Scanner;

class Main {
  public static void main(String[] args) throws IOException {
  
    Scanner ler = new Scanner(System.in);
    //declaração de variavel
    String nome;
    
    //leitura de variavel
    System.out.printf("informe seu nome: ");
    
    //processamento de leitura
    nome = ler.nextLine();
    //saida de imfomação
     System.out.printf("Olá, %s", nome);
    
  }
}