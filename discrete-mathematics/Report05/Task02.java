import java.util.*;

public class Task02 {

    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--------------Constraint--------------");
        System.out.println("n, r은 양의 정수 (0 <= r <= n)\n");
        
        // 입력 받기
        System.out.println("--------------Input--------------");
        System.out.print("n = ");
        int n = sc.nextInt();

        System.out.print("r = ");
        int r = sc.nextInt();

        sc.close();

        //  방문 체크를 위한 boolean 배열
        boolean[] visited = new boolean[n];

        //  배열 생성하여 값 초기화
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = i+1;
        }


        System.out.println("\n--------------result--------------");

        //  combination 출력 함수
        //  백트레킹 기법을 활용하여 구현
        combination(arr, visited, 0, n, r);
    }

    private static void combination(int[] arr, boolean[] visited, int start, int n, int r) {
        if (r == 0) {
            print(arr, visited, n);
            return;
        }

        for (int i = start; i<n; i++) {
            visited[i] = true;
            combination(arr, visited, i + 1, n, r - 1);
            visited[i] = false;
        }
    }

    private static void print(int[] arr, boolean[] visited, int n) {
        for (int i = 0; i<n; i++) {
            if (visited[i]) {
                System.out.print(arr[i] + " ");
            }
        }
        System.out.println();
    }
}