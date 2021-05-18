import java.util.*;

public class Task02 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        
        System.out.println("--------------Constraint--------------");
        System.out.println("a, b는 양의 정수\n");
        
        // 입력 받기
        System.out.println("--------------Input--------------");
        System.out.print("a = ");
        int a = sc.nextInt();

        System.out.print("b = ");
        int b = sc.nextInt();

        sc.close();

        //  비재귀적 방법을 이용한 최대공약수 구하는 함수
        System.out.println( "\n비재귀적 함수 : " + gcd_loop( a, b ) );

        //  재귀적 방법을 이용한 최대공약수 구하는 함수
        System.out.println( "재귀적 함수 : " + gcd_recursion( a, b ) );       
    }
    
    private static int gcd_loop(int a, int b) {
        if(b == 0){
            return a;
        }else{
            return gcd_loop(b, a%b);
        }
    }

    private static int gcd_recursion(int a, int b) {
        int tmp, n;
 
        if(a<b){
            tmp = a;
            a = b;
            b = tmp;
        }
        
        while(b!=0){
            n = a%b;
            a = b;
            b = n;
        }
        return a;
    }
}