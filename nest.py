# 嵌套序列或元组  和Java中的二维数组一样。

# High Scores 2.0
# 演示嵌套序列

scores = []

choice = None

while choice != "0":

    print(
    """
    High Scores 2.0

    0 - Quit
    1 - List Scores
    2 - Add a Scores
    """
    )


    choice = input("Choice: ")
    print()

    # 退出
    if choice == "0":
        print("Good Bye.")
        input("\n\nPress the enter key to exit.")

    # 显示高分表
    elif choice == "1":
        print("High Scores\n")
        print("NAME\t\t\tSCORE")
        for entry in scores:  # entry 条目，记录，入口
            score, name = entry
            print(name, "\t\t", score)

    # 添加得分记录，用元组的方式添加得分记录
    elif choice == "2":
        name = input("What is the player's names?: ")
        score = int(input("What score did the player get?: "))
        entry = (score, name)
        scores.append(entry)
        scores.sort(reverse=True)
        scores = scores[:5] # 只保留最高的5条得分数
    # 无效选项
    else:
        print("Sorry, But", choice, "isn't a valid choive.")
        
