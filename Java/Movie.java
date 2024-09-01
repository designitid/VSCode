//Creator: DANI ANTO PAKPAHAN
//IDE    : Visual Studio Code

class Movies{
    String Title;
    String Genre;
    double Rating;
}

public class Movie{
    public static void main (String[] args){
        Movies movie1 = new Movies();
        Movies movie2 = new Movies();
        Movies movie3 = new Movies();

        movie1.Title  = "Indonesia";
        movie1.Genre  = "Action";
        movie1.Rating = 10.0;

        movie2.Title  = "Blue Archive";
        movie2.Genre  = "Kids";
        movie2.Rating = 8.0;

        movie3.Title  = "Hiroshima";
        movie3.Genre  = "History";
        movie3.Rating = 8.1;

        System.out.println("\nTitle  : "+movie1.Title);
        System.out.println("Genre  : "+movie1.Genre);
        System.out.println("Rating : "+movie1.Rating);
        
        System.out.println("\nTitle  : "+movie2.Title);
        System.out.println("Genre  : "+movie2.Genre);
        System.out.println("Rating : "+movie2.Rating);
       
        System.out.println("\nTitle  : "+movie3.Title);
        System.out.println("Genre  : "+movie3.Genre);
        System.out.println("Rating : "+movie3.Rating);
    }

}