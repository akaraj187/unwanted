public class Student {
    String name;
    int id;
    int age;
    double CGPA;
    public static String U ="KLETECH University";
//create a method to display student details


// create a method to display student name with maximum CGPA by passing array of objects

    public static void findMaxCGPA(Student[] students) {
        double maxCGPA = 0;
        String maxName = "";
        for (Student s : students) {
            if (s.CGPA > maxCGPA) {
                maxCGPA = s.CGPA;
                maxName = s.name;
            }
        }
        System.out.println("Student with maximum CGPA: " + maxName + " with CGPA: " + maxCGPA);
    }
    // Constructor to initialize a Student object
    Student(String name, int id,int age,double CGPA) {
        this.name = name;
        this.id = id;
        this.age=age;
        this.CGPA=CGPA;
    }

    // Method to display student details
    public void display() {
        System.out.println("Name: " + name + ", ID: " + id + "AGE:"+age +"CGPA:"+CGPA+"University:"+U);
    }

   public static void main(String[] args){
   //Create an array of Student objects
   Student[] students = {
       new Student("a", 1, 12, 9),
       new Student("b", 2, 13, 8),
       new Student("c", 3, 14, 7)
   };
   // Display all student details
   for (Student s : students) {
       s.display();
   }
   // Find and display the student with maximum CGPA
   findMaxCGPA(students);
}
}
