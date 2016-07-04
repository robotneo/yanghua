# High Scores程序
# 演示列表方法

scores = []  # scores 得分
choice = None

while choice != "0":
    
    print(
        """
    High Scores


    0 - Exit
    1 - Show Scores
    2 - Add a score
    3 - Remove a Score
    4 - Sort Scores
    
        """
        )

    choice = input("Choice: ")
    print()

    # 退出
    if choice == "0":
        print("Good-bye.")
        input("\n\nPress the enter key to exit.")
        
    # 列出最高得分表
    elif choice == "1":
        print("High Scores")
        for score in scores:
            print(score)

    # 添加得分记录
    elif choice == "2":
        score = int(input("What score did you get? : "))
        scores.append(score)
    # 删除得分记录
    elif choice == "3":
        score = int(input("Remove which score? : "))
        if score in scores:
            scores.remove(score)
        else:
            print(score, "isn't in the high scores list.")

    # 对得分记录进行排序
    elif choice == "4":
        scores.sort(reverse=True)

    # 其他位置选项
    else:
        print("Sorry, But", choice, "isn't a valid choice.")

    
