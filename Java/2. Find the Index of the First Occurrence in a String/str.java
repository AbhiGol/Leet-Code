public class str {
    public static void main(String[] args) {
        String str = "Hello, World!";
        String substring = "World";

        int index = str.indexOf(substring);

        if (index != -1) {
            System.out.println("Substring found at index: " + index);
        } else {
            System.out.println("Substring not found.");
        }
    }
}
