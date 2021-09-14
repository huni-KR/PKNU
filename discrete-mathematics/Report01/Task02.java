import java.io.*;
import java.util.*;

public class Task02 {
    
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //  중복된 값을 저장하지 않기 위해 set 자료구조 사용
        Set<Integer> set = new HashSet<>();
        
        //  문자열을 읽어서 StringTokenizer를 활용하여 set에 데이터 저장
        System.out.print( "집합 A 원소 입력 : " );
        readString(set, br.readLine());

        //  저장한 기본 집합 출력하기
        System.out.print( "A = " );
        printSet(set);

        //  효율적인 방문 체크를 위해 set -> array
        int[] arr = setToArray(set);
        boolean[] visited = new boolean[set.size()];

        //  재귀함수를 통해 powerset 구현
        powerSet(arr, visited, arr.length, 0);
    }


    private static void powerSet(int[] arr, boolean[] visited, int n, int idx) {
        if(idx == n) {
            print(arr, visited, n);
            return;
        }
     
        visited[idx] = false;
        powerSet(arr, visited, n, idx + 1);
     
        visited[idx] = true;
        powerSet(arr, visited, n, idx + 1);
    }

    static void print(int[] arr, boolean[] visited, int n) {
        System.out.print("{ ");
        for (int i = 0; i < n; i++) {
            if (visited[i] == true)
                System.out.print(arr[i] + " ");
        }
        System.out.println("}");
    }
    
    private static int[] setToArray(Set<Integer> set) {
        int[] result = new int[set.size()];
        int index = 0;
        for(int i : set){
            result[index++] = i;
        }
        return result;
    }

    private static void printSet(Set<Integer> set) {
        System.out.print("{ ");
        for(int n : set){
            System.out.print(n + " ");
        }
        System.out.println("}");
    }

    private static void readString(Set<Integer> set, String str) {
        StringTokenizer st = new StringTokenizer(str, " ");
        while(true){
            int n = Integer.parseInt(st.nextToken());
            if( n == 0 )
                break;
            set.add(n);
        }
    }
}