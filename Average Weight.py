import java.util.Scanner;
public class weight{
    public static void main(String args[]){
        Scanner sc=new Scanner(System.in);
        int a,b,c,avg;
        avg=sc.nextInt();
        a=sc.nextInt();
        b=sc.nextInt();
        c=(3*avg)-(a+b);
        System.out.println(c);
        sc.close();
    }
}