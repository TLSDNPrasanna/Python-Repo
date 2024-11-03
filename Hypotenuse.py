import java.util.Scanner;
public class hypo{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int y=sc.nextInt();
        double hy=Math.sqrt((x*x)+(y*y));
        float hypo=(float)hy;
        System.out.printf("%.2f",hypo);
    }
}