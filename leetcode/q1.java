class Solution {
public:
    bool isNumber(string s) {
        int i = 0;
        while (i < s.size() && s[i] == ' ') i++;//排除前边空格
        int j = s.size()-1;
        while (j >= 0 && s[j] == ' ') j--;//排除后边空格
        s = s.substr(i, j-i+1);//截取所剩的字符串

        if (s[0] == '+' || s[0] == '-') s = s.substr(1);//检查开头是否为运算符
        if (s[0] == '.' && s.size() == 1 || s.empty() ) return false;//排除单字符和字符组合的情况

        int e = 0, dot = 0;//统计‘.’的数量和e的数量
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] >= '0' && s[i] <= '9');//字符为数字继续
            else if (s[i] == '.')//字符为'.'判断是否有e或者点的数量是否大于1
            {
                dot ++;
                if (e || dot > 1) return false;
            }
            else if (s[i] == 'e' || s[i] == 'E')//字符为e或者‘E’时
            {
                e++;
                if (i + 1 == s.size() || e > 1 || !i || i == 1 && s[0] == '.') return false;//排除e结尾、多个e、e开头、e和点同时出现的情况
                if (s[i+1] == '+' || s[i+1] == '-')//e后边接着跟运算符的情况
                {
                    if (i+2 == s.size()) return false;//运算符后边没有跟数字
                    i++; 
                }
            }
            else return false;//其他情况直接判错
        } 
        return true;
    }
};
