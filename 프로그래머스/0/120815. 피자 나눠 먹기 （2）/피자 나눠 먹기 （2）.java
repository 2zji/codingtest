class Solution {
    public int solution(int n) {
        return lcm(6, n) / 6;
    }
    private int lcm(int a, int b){
        return (a*b) / gcd(a, b);
    }
    private int gcd(int a, int b){
        return b == 0 ? a : gcd(b, a % b);
    }
}