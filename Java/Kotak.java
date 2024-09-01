public class Kotak {

    private String bahan;
    private int panjang;
    private int lebar;
    private int tinggi;
    private String warna;
  
    public Kotak(String bahan, int panjang, int lebar, int tinggi, String warna) {
      this.bahan = bahan;
      this.panjang = panjang;
      this.lebar = lebar;
      this.tinggi = tinggi;
      this.warna = warna;
    }
  
    public int getVolume() {
      return panjang * lebar * tinggi;
    }
  
    public void buka() {
      System.out.println("Kotak " + warna + " dibuka");
    }
  
    public void tutup() {
      System.out.println("Kotak " + warna + " ditutup");
    }

  
  }
  