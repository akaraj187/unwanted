public class Mobile{
    int Model;
    String Brand;

    Mobile(int M,String B){
        Model=M;
        Brand=B;
    }

    void Display()
    {
        System.out.println("MODEL="+Model);
        System.out.println("BRAND="+Brand);
    }

public static void main(String[] args){
    Mobile M=new Mobile(1,"MI");
    M.Display();
}
}
