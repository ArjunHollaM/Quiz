import answers

l=["1)50-50","2)Pass","3)Eliminate one"]
def pass_question(cha):
    print("Pass activated...awarded 3 points")
    print("The right option for this question is "+answers.ans[cha])
def half(cha):
    x=answers.ha[cha]
    print(x)
    n=input()
    if n.isalpha():
        if answers.ans[cha]==n.lower():
            return "Correct"
        else:
            return "Wrong"
    else:
        return "Wrong"

def eliminate(cha):
    y=answers.el[cha]
    print(y)
    n=input()
    if n.isalpha():
        if answers.ans[cha]==n.lower():
            return "Correct"
        else: return "Wrong"
    else:
        return "Wrong"

