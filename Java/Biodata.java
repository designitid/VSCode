import java.util.Scanner;

public class Biodata {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Masukkan nama: ");
        String nama = scanner.nextLine();

        System.out.print("Masukkan umur Anda: ");
        String umur = scanner.nextLine();
        
        System.out.print("Masukkan alamat Anda: ");
        String alamat = scanner.nextLine();

        System.out.print("Masukkan pekerjaan Anda: ");
        String pekerjaan = scanner.nextLine();

        System.out.println("Nama: " + nama);
        System.out.println("Umur: " + umur);
        System.out.println("Alamat: " + alamat);
        System.out.println("Pekerjaan: " + pekerjaan);
    }
}
