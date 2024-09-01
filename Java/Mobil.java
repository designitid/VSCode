public class Mobil {

    private String merek;
    private String model;
    private int tahun;
    private String tipeTransmisi;
    private int kapasitasMesin;
  
    public Mobil(String merek, String model, int tahun, String tipeTransmisi, int kapasitasMesin) {
      this.merek = merek;
      this.model = model;
      this.tahun = tahun;
      this.tipeTransmisi = tipeTransmisi;
      this.kapasitasMesin = kapasitasMesin;
    }
  
    public void nyalakanMesin() {
      System.out.println("Mesin mobil " + merek + " dinyalakan");
    }
  
    public void matikanMesin() {
      System.out.println("Mesin mobil " + merek + " dimatikan");
    }
  
  }
  