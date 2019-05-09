import java.io.*;

public class CalculateNumberOfFilesInFolder {
        public static void main(String[] args) {
                File f = new File("C:/src/flutter/.github"); // Add file location from here
                int count = 0;
                for (File file : f.listFiles()) {
                        if (file.isFile()) {
                                count++;
                        }
                }
                System.out.println("Number of files: " + count);
        }
}