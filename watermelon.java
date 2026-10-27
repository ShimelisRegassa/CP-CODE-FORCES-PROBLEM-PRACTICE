import java.util.Scanner;
class watermelon {
    public static void main(String[] args) {
        Scanner in =new Scanner(System.in);
        System.out.println("WEIGHT OF THE WATERMELON :");
        int weight=in.nextInt();
        if(weight%2==1 && weight!=2){
            System.out.println("NO");
            
        }
        else{
            System.out.println("YES");
        }
        in.close();
    }
}