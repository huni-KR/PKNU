import java.util.*;

public class Task02 {
    
    public static void main(String[] args){
            
        Scanner sc = new Scanner(System.in);
        
        System.out.println("\n--------------Constraint--------------");
        System.out.println("2 <= a < m\t0 <= c < m\t0 <= s < m\n");
        
        // m 
        System.out.println("--------------Input--------------");
        System.out.print("modulus m = ");
        int m = sc.nextInt();
`
        System.out.print("multiflier a = ");
        int a = sc.nextInt();

        System.out.print("increment c = ");
        int c = sc.nextInt();

        System.out.print("seed s = ");
        int s = sc.nextInt();

        System.out.print("number of Random numbers n = ");
        int n = sc.nextInt();
        
        sc.close();

        int[] arr = new int[n];
        arr[0] = ( a * s + c ) % m;

        for(int i=1; i<arr.length; i++){
            arr[i] = ( a * arr[i-1] + c ) % m;
        }

        System.out.println("\n-------Output-------");
        for(int i=0; i<n; i++){
            System.out.println( "x[" + ( i + 1 ) + "] = " + arr[i] );
        }

    }
}
