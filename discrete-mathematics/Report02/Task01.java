import java.util.*;

public class Task01 {
    
    public static void main(String[] args){

        Scanner sc = new Scanner(System.in);

        // 크기가 11 배열
        int[] arr = new int[11];

        // 방문체크를 위한 배열
        boolean[] visit = new boolean[11];

        for(int i=0; i<10; i++){
            System.out.print( (i+1) + "번째 정수 입력 : " );

            // 사용자로부터 정수 입력 받기
            int value = sc.nextInt();

            // 모듈러 연산
            int index = value % 11;

            // 방문하지 않은 index 즉 비어있는 해쉬 배열
            if( !visit[index] ){
                arr[index] = value;
                visit[index] = true;
            }
            // 이미 방문한 index 이미 입력된 정수가 
            else{
                System.out.println("Collision!");            
            }

            // 배열 상태 출력
            printArray(arr);
        }
        sc.close();
    }

    private static void printArray(int[] arr) {
        System.out.println("---------------해쉬 배열---------------");
        for(int i=0; i<arr.length; i++){
            System.out.print( arr[i] + " " );
        }
        System.out.println("\n----------------------------------------\n");
    }
}
