import java.io.*;
import java.util.*;

public class Task01 {
    
    public static void main(String[] args) throws IOException{

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        //  중복된 값을 저장하지 않기 위해 set 자료구조 사용
        Set<Integer> set1 = new HashSet<>();
        Set<Integer> set2 = new HashSet<>();
        
        //  문자열을 읽어서 StringTokenizer를 활용하여 set에 데이터 저장
        System.out.print( "집합 A 원소 입력 : ");
        readString(set1, br.readLine());
        System.out.print( "집합 B 원소 입력 : ");
        readString(set2, br.readLine());

        br.close();

        //  저장한 기본 집합 출력하기
        System.out.print( "A = " );
        printSet(set1);
        System.out.print( "B = " );
        printSet(set2);

        //  2개의 Set을 순환하며 A B 합집합 생성
        Set<Integer> union = calcUnion(set1, set2); 
        //  union 집합 출력
        System.out.print( "A ∪ B = " );
        printSet(union);

        //  2개의 Set을 순환하며 A - B 집합 생성
        Set<Integer> difference1 = calcDifferenceAndIntersection(set1, set2, true);
        //  A - B 집합 출력
        System.out.print( "A - B = " );
        printSet(difference1);

        //  2개의 Set을 순환하며 B - A 집합 생성
        Set<Integer> difference2 = calcDifferenceAndIntersection(set2, set1, true);
        //  B - A 집합 출력
        System.out.print( "B - A = " );
        printSet(difference2);

        //  2개의 Set을 순환하며 A B 교집합 생성
        Set<Integer> intersection = calcDifferenceAndIntersection(set1, set2, false);
        //  A B 교집합 출력
        System.out.print( "A ∩ B = " );
        printSet(intersection);
    }

    private static Set<Integer> calcDifferenceAndIntersection(Set<Integer> set1, Set<Integer> set2, boolean b) {
        Set<Integer> result = new HashSet<>();
        for(int i : set1){
            boolean flag = true;
            for(int j : set2){
                if( i == j ){
                    flag = false;
                }
            }
            if( b == flag )  result.add(i);            
        }
        return result;
    }

    private static Set<Integer> calcUnion(Set<Integer> set1, Set<Integer> set2) {
        Set<Integer> result = new HashSet<>();
        for(int n : set1)
            result.add(n);
        for(int n : set2)
            result.add(n);
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
