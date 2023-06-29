public class Reverse {
    public static void main(String[] args) {
        String str;
        str = "Abhi";
        System.out.println("Reverse of a String '" + str + "' is  :");
        for (int j = str.length(); j > 0; --j) {
            System.out.print(str.charAt(j - 1));
        }
    }
}
