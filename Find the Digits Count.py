import java.util.Scanner;
public class count{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int n=sc.nextInt();
        int c=0;
        while(n>0){
            int r=n%10;
            c=c+1;
            n=n/10;
        }
        System.out.println(c);
}
}