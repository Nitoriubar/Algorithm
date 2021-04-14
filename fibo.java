import java.util.*;

public class Fibo {
  
   long[] fibo_array = new long[100];
  
   public static void main(String[] args) {
     for(int i=1; i<=n; i++){
       if(n == 1 || n==2){
         fibo_array[i] = 1;
       }
       fibo_array[i] = fibo_array[i-1] + fibo_array[i-2];
     }
     System.out.println(fibo(100));
  }
}
