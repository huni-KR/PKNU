import java.util.*;

public class Task03 {

    public static void main(String[] args) {
    
        Scanner sc = new Scanner(System.in);
        
        System.out.println("--------------Constraint--------------");
        System.out.println("n은 양의 정수\n");
        
        // 입력 받기
        System.out.println("--------------Input--------------");
        System.out.print("n = ");
        int n = sc.nextInt();

        sc.close();

        //  배열 생성하여 값 초기화
        int[] arr = new int[n];
        for(int i=0; i<n; i++){
            arr[i] = i+1;
        }

        System.out.println("\n--------------result--------------");

        //  permutation 출력 함수
        //  재귀함수를 활용하여 구현
        permutation(arr, 0);
    }
    public static void permutation(int[] arr, int pivot) { 
        if (pivot == arr.length) { 
            print(arr); 
            return; 
        } 
        
        for (int i = pivot; i < arr.length; i++) { 
            swap(arr, i, pivot); 
            permutation(arr, pivot + 1); 
            swap(arr, i, pivot); 
        } 
    }
    
    public static void swap(int[] arr, int i, int j) {         
        int temp = arr[i]; 
        arr[i] = arr[j]; 
        arr[j] = temp; 
    } 
    
    public static void print(int[] arr) { 
        for (int i = 0; i < arr.length; i++) { 
            if (i == arr.length - 1) {
                System.out.println(arr[i]); 
            } else {
                System.out.print(arr[i] + " ");
            }
        }
    }
}