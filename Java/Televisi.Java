public class Televisi {

    private String merek;
    private int ukuranLayar;
    private boolean smartTV;
  
    public Televisi(String merek, int ukuranLayar, boolean smartTV) {
      this.merek = merek;
      this.ukuranLayar = ukuranLayar;
      this.smartTV = smartTV;
    }
  
    public void nyalakan() {
      System.out.println("Televisi " + merek + " dinyalakan");
    }
  
    public void matikan() {
      System.out.println("Televisi " + merek + " dimatikan");
    }
  
  
  }
  