import java.util.Scanner;
public class avg{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int[] a=new int[n];
        for (int i=0;i<n;i++){
            a[i]=sc.nextInt();
        }
        float s=0;
        for (int i=0;i<n;i++){
            s=s+a[i];
        }
        float avg=s/n;
        System.out.printf("%.2f",avg);
    }
}