# Geek Translator 程序(字典笔记程序)

# 出现一个菜单系统，选择做什么事。
# 定义一个字典变量,自己定义了一些单词，不过不能存放太多数据，不然会引起内存的泄露。

geek = {"term":"术语;学期;期限;条款",
        "geek":"极客;野人","entry":"进入;条目;登记;入口", "valid":"有效的;合法的",
        "reverse":"背面;相反;倒退;失败", "trade":"贸易;交易;买卖", "crossbow":"弩;石弓",
        "necklace":"项链", "gems":"宝石", "helmet":"钢盔;头盔", "hang":"悬挂;垂下;装饰;绞死",
        "hint":"提示", "exerise":"练习", "jumble":"混乱;杂乱", "inventory":"存货;详细目录;财产清册"
        }

choice = None

while choice != "0":

    print(

    """
    Geek Translator

    0 - Quit
    1 - Look Up a Geek Translator
    2 - Add a Geek Translator
    3 - Redefine a Geek Translator
    4 - Delete a Geek Translator
    """
    )

    choice = input("Choice: ")
    print()

    # 退出
    if choice == "0":
        print("Good-bye")
        input("\n\nPress the enter key to exit.")

    # 获取值
    elif choice == "1":
        term = input("What term do you want me to translate?: ")
        if term in geek:
            definition = geek[term]
            print("\n<",term,"> means: ", definition)
        else:
            print("\nSorry, I don't know", term)


    # 增加键值对，添加一对新的术语
    elif choice == "2":
        term = input("What term do you want me to add?: ")
        if term not in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been added.")
        else:
            print("\nThat term already exists! Try redefining it.")

    # 重新定义某个词的意思
    elif choice == "3":
        term = input("What term do you want me to redefine?: ")
        if term in geek:
            definition = input("\nWhat's the definition?: ")
            geek[term] = definition
            print("\n", term, "has been redefine.")
        else:
            print("\nThat's term doesn't exist! Try adding it.")

    # 删除一个键值对，删除术语
    elif choice == "4":
        term = input("What term do you want me to delete?: ")
        if term in geek:
            del geek[term]  # 删除一个术语，就是指定删除那个键del[term]
            print("\nOkay, I deleted", term)
        else:
            print("\nI can't do that!", term, "doesn't exist in the dictionary")

    #结束程序
    else:
        print("\nSorry, But", choise, "isn't a vaild choice.")

    input("\n\nPress the enter key to continue.")
