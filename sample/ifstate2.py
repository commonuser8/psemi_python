# 数学の成績評価
# 変数 math の値が...
# 80 以上: "S",
# 60 以上 80 未満: "A",
# 60 未満: "B"
math = 70
if math >= 80:
    print("S")
elif math >= 60:
    print("A")
else:
    print("B")

'''
# Javaで書いた同じコード
# pythonの方が全体的に簡略化されている（書きやすい）

public class Main {
    public static void main(String[] args) {
        int math = 70;
        if (math >= 80) {
            System.out.println("S");
        } else if (math >= 60) {
            System.out.println("A");
        } else {
            System.out.println("B");
        }
    }
}
'''
