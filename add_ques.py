import json

#list of questions,options, answers
# questions = ["Which is the highest peak in the world?","Where was Gautam Buddha born?","What is capital city of nepal?","How tall is Mt.Everest"]
# answers = [["K2","Kanchanjunga","Mount Everest","Annapurna"],["Nepal","India","Bhutan","China"],["Pokhara","Kathmandu","Chitwan","Biratnagar"],["8848","8848.48","8848.86","8848.46"]]
# correctans =[3,1,2,3]
questions=[]
answers=[]
correctans=[]

def adding_question():
    quiz_data=[]
    que=input("Enter question: ")
    questions.append(que)
    ans=[]
    for a in range(4):
        ans.append(input(f"Enter option {a+1}: "))
    answers.append(ans)
    correct=int(input("Enter which option is correct? "))
    correctans.append(correct)
    for i in range(len(questions)):
        quiz_data.append({
            "questions":questions[i],
            "answers":answers[i],
            "correctans":correctans[i]
        })

    s=json.dumps(quiz_data)
    with open("E:\\Python Examples\\Quiz game\\question_set.json","w") as f:
        f.write(s)