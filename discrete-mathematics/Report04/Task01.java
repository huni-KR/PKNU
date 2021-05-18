import java.util.*;

public class Task01 {

    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--------------Constraint--------------");
        System.out.println("a, n, z는 양의 정수\n");
        
        // 입력 받기
        System.out.println("--------------Input--------------");
        System.out.print("a = ");
        int a = sc.nextInt();

        System.out.print("n = ");
        int n = sc.nextInt();

        System.out.print("z = ");
        int z = sc.nextInt();

        sc.close();
        
        //  거듭제곱 누승수 계산 함수
        System.out.println( "\nresult : " + exp_mod_via_repeated_squaring_loop( a, n, z ) );
    }    
    

    private static int exp_mod_via_repeated_squaring_loop(int a, int n, int z) {
        int result = 1;
        int x = a % z;

        while( n > 0 ){
            if( n % 2 == 1 ){
                result = ( result * x ) % z;                
            }
            x = ( x * x ) % z;
            n = (int) Math.floor((double)(n/2));
        }
        return result;
    }
}
