import java.util.Scanner;
import java.util.*;

public class EnglishToMorse 
{

   public static void main(String[] args) 
   {
      Scanner input = new Scanner(System.in);
      System.out.println("<English to Morse>");
      
      System.out.print("Typing English : ");
      String text = input.nextLine();
      char[] letter = text.toCharArray();
      
      System.out.println();
      
      System.out.print("Result : ");
      for(int i = 0; i<letter.length; i++)
      {
         translate(i, letter);
      }
   }
   
   public static void translate(int i, char[] letter)
   {
      if(letter[i] == 'a' || letter[i] == 'A')
      {
         System.out.print(".-");
      }
      else if(letter[i] == 'b' || letter[i] == 'B')
      {
         System.out.print("-...");
      }
      else if(letter[i] == 'c' || letter[i] == 'C')
      {
         System.out.print("-.-.");
      }
      else if(letter[i] == 'd' || letter[i] == 'D')
      {
         System.out.print("-..");
      }
      else if(letter[i] == 'e' || letter[i] == 'E')
      {
         System.out.print(".");
      }
      else if(letter[i] == 'f' || letter[i] == 'F')
      {
         System.out.print("..-.");
      }
      else if(letter[i] == 'g' || letter[i] == 'G')
      {
         System.out.print("--.");
      }
      else if(letter[i] == 'h' || letter[i] == 'H')
      {
         System.out.print("....");
      }
      else if(letter[i] == 'i' || letter[i] == 'I')
      {
         System.out.print("..");
      }
      else if(letter[i] == 'j' || letter[i] == 'J')
      {
         System.out.print(".---");
      }
      else if(letter[i] == 'k' || letter[i] == 'K')
      {
         System.out.print("-.-");
      }
      else if(letter[i] == 'l' || letter[i] == 'L')
      {
         System.out.print(".-..");
      }
      else if(letter[i] == 'm' || letter[i] == 'M')
      {
         System.out.print("--");
      }
      else if(letter[i] == 'n' || letter[i] == 'N')
      {
         System.out.print("-.");
      }
      else if(letter[i] == 'o' || letter[i] == 'O')
      {
         System.out.print("---");
      }
      else if(letter[i] == 'p' || letter[i] == 'P')
      {
         System.out.print(".--.");
      }
      else if(letter[i] == 'q' || letter[i] == 'Q')
      {
         System.out.print("--.-");
      }
      else if(letter[i] == 'r' || letter[i] == 'R')
      {
         System.out.print(".-.");
      }
      else if(letter[i] == 's' || letter[i] == 'S')
      {
         System.out.print("...");
      }
      else if(letter[i] == 't' || letter[i] == 'T')
      {
         System.out.print("-");
      }
      else if(letter[i] == 'u' || letter[i] == 'U')
      {
         System.out.print("..-");
      }
      else if(letter[i] == 'v' || letter[i] == 'V')
      {
         System.out.print("...-");
      }
      else if(letter[i] == 'w' || letter[i] == 'W')
      {
         System.out.print(".--");
      }
      else if(letter[i] == 'x' || letter[i] == 'X')
      {
         System.out.print("-..-");
      }
      else if(letter[i] == 'y' || letter[i] == 'Y')
      {
         System.out.print("-.--");
      }
      else if(letter[i] == 'z' || letter[i] == 'Z')
      {
         System.out.print("--..");
      }
      else if(letter[i] == '0')
      {
         System.out.print("-----");
      }
      else if(letter[i] == '1')
      {
         System.out.print(".----");
      }
      else if(letter[i] == '2')
      {
         System.out.print("..---");
      }
      else if(letter[i] == '3')
      {
         System.out.print("...--");
      }
      else if(letter[i] == '4')
      {
         System.out.print("....-");
      }
      else if(letter[i] == '5')
      {
         System.out.print(".....");
      }
      else if(letter[i] == '6')
      {
         System.out.print("-....");
      }
      else if(letter[i] == '7')
      {
         System.out.print("--...");
      }
      else if(letter[i] == '8')
      {
         System.out.print("---..");
      }
      else if(letter[i] == '9')
      {
         System.out.print("----.");
      }
      else if(letter[i] == ' ')
      {
         System.out.print(" ");
      }
      else
      {
         System.out.print("Error");
      }
   }
}