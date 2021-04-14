import java.util.*;

public class Fibo {
  
   public static long[] fibo_array = new long[100]; 
  
   public static void main(String[] args) {
     int n = 100; 
     
     for(int i=1; i<=n; i++){
       //1,2번째 피보나치 수의 값 = 1
       if(n == 1 || n==2){   
         fibo_array[i] = 1;
       }
       fibo_array[i] = fibo_array[i-1] + fibo_array[i-2];
     }
     System.out.println(fibo_array[n]);
  }
}
