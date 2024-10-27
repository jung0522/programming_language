class PrintStr {
    int n = 3;
    String s = "abc";
    
    public String toString() {
        return "n = " + n + ", s = " + s;
    }
    
    public static void main(String[] args) {
        PrintStr ps = new PrintStr();
        System.out.println(ps);
    }
}