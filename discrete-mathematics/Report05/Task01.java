import java.util.*;

public class Task01 {

    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--------------Constraint--------------");
        System.out.println("n은 양의 정수\n");
        
        // 입력 받기
        System.out.println("--------------Input--------------");
        System.out.print("n = ");
        int n = sc.nextInt();

        sc.close();

        //  로봇의 걸음 경우의 수 계산 함수
        //  동적 계획법(Dynamic Programming)을 활용하여 구현
        System.out.println( "\nresult : " + robotWalk(n) );        
    }

    private static int robotWalk(int n){
        if( n == 1 || n == 2 ){
            return n;
        }else{
            int[] arr = new int[n+1];

            arr[1] = 1;
            arr[2] = 2;

            for(int i=3; i<=n; i++){
                arr[i] = arr[i-1] + arr[i-2];
            }
            return arr[n];    
        }
    }
}