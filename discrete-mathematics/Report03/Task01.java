import java.io.*;
import java.util.*;

public class Task01 {

    static int[] arr;

    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        arr = new int[n];

        // 입력 받은 문자열 공백을 기준으로 문자열 나누기
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");
        br.close();

        // 입력 받은 정수 배열에 저장
        for(int i=0; i<n; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        System.out.println( "\tBubble Sort" );

        System.out.println( "정렬전 : ");
        //  배열 출력
        printArray();

        //  Bubble Sort
        BubbleSort();

        System.out.println( "\n\n정렬후 : ");
        //  배열 출력
        printArray();
    }

    private static void printArray() {
        for(int i=0; i<arr.length; i++){
            System.out.print( arr[i] + " " );
        }
    }

    private static void BubbleSort() {
        for(int i=0; i<arr.length; i++){
            for(int j=0; j<arr.length -(i+1); j++){                
                if( arr[j] > arr[j+1] ){                    
                    int tmp = arr[j+1];
                    arr[j+1] = arr[j];
                    arr[j] = tmp;
                }
            }
        }
    }
}