import java.util.Random;

public class dadu {

    public static void main(String[] args) {
        Random random = new Random();

        int dadu1 = random.nextInt(6) + 1;
        int dadu2 = random.nextInt(6) + 1;

        System.out.println("Hasil lempar dadu 1: " + dadu1);
        System.out.println("Hasil lempar dadu 2: " + dadu2);
        System.out.println("Total nilai dadu: " + (dadu1 + dadu2));
    }

}
