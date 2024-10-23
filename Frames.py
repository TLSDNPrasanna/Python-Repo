import java.util.Scanner;
public class wf{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int n,m,x;
        n=sc.nextInt();
        m=sc.nextInt();
        x=sc.nextInt();
        int p=2*(n+m);
        System.out.println(p*x);
    }
}