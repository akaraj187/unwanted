public class Employee{
    int EmployeeID;
    String Employee_Name;
    double salary;
    String Company_Name;


    Employee(int EID,String N,double S,String CN){
        EmployeeID=EID;
        Employee_Name=N;
        salary=S;
        Company_Name=CN;
    }

    void Display(){
        System.out.println("Employee Details:");
        System.out.println("Employee ID="+EmployeeID);
        System.out.println("Employee_Name="+Employee_Name);
        System.out.println("Employee Salary="+salary);
        System.out.println("Company Name="+Company_Name);
    }

    void Total_Salary(Employee e,Employee e1){
        
        
        double T=e.salary+e1.salary;
        System.out.println("Total Salary of Two Employees ="+T);
    }
    public static void main(String [] args)
    {
        Employee e1=new Employee(1,"Aa",1000,"XYZ");
        Employee e2=new Employee(2,"Bb",2000,"ABC");

        e1.Display();
        e2.Display();

       e1.Total_Salary(e1,e2);
    }
}
