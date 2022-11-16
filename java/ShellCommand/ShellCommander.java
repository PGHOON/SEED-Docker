import java.io.BufferedReader;
import java.io.InputStream;
import java.io.InputStreamReader;


public class ShellCommander {

public static void main(String[] args)throws Exception {

       String command1 = "docker run -d -p 2222:22 --name test2  ubuntu /bin/bash";
       shellCmd(command1);

 }

 public static void shellCmd(String command)throws Exception {

       Runtime runtime = Runtime.getRuntime();
       Process process = runtime.exec(command);
       InputStream is = process.getInputStream();
       InputStreamReader isr =new InputStreamReader(is);
       BufferedReader br =new BufferedReader(isr);
       String line;

       while((line = br.readLine()) != null) {
              System.out.println(line);
       }
 }

}