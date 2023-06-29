public class Alphabet {
    public static void main(String[] args) {
        int i = 0;
        char ch = 'A';
        if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch == 'u' || ch == 'A' || ch == 'E' || ch == 'I'
                || ch == 'O' || ch == 'U') {
            System.out.println("Entered character " + ch + " is  Vowel");
        } else if ((ch >= 'a' && ch <= 'z') || (ch >= 'A' && ch <= 'Z'))
            System.out.println("Entered character " + ch + " is Consonant");
        else
            System.out.println("Not an alphabet");
    }
}
