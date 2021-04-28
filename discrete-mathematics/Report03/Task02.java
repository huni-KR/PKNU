import java.io.*;
import java.util.*;

public class Task02 {

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

        System.out.println( "\tInsertion Sort" );

        System.out.println( "정렬전 : ");
        //  배열 출력
        printArray();

        //  Insertion Sort
        InsertionSort();

        System.out.println( "\n\n정렬후 : ");
        //  배열 출력
        printArray();
    }

    private static void printArray() {
        for(int i=0; i<arr.length; i++){
            System.out.print( arr[i] + " " );
        }
    }

    private static void InsertionSort() {
        for(int i=1; i<arr.length; i++){
            
            int temp = arr[i];
            int aux = i - 1;

            while( (aux >= 0) && ( arr[aux] > temp ) ) {

                arr[aux+1] = arr[aux];
                aux--;
            }
            arr[aux + 1] = temp;
        }        
    }
}