import json
from datetime import datetime
def load_data():
    try:
        with open("money.json","r",encoding = "utf-8") as f:
            records = json.load(f)
    except FileNotFoundError:
        records = []
    return records
def save_data(data):
     with open("money.json","w",encoding = "utf-8") as f:
                         json.dump(data,f,ensure_ascii=False)
def main():
    records = load_data()    
    while True:
        print("1.记账")
        print("2.查询")
        print("3.退出")
        print("4.今日统计")
        print("5.删除最后一条")
        option = input("请选择操作：")
        if option == "1":
            print("记账功能")
            money = input("请输入金额：")
            note = input("请输入备注：")
            money = float(money)
            dic = {"金额": money,"备注": note}
            records.append(dic)
            save_data(records)
            print("记账成功")
        elif option == "2":
            print("查询功能")
            if records == []:
                print("暂无记账记录")
            else:
                all_money = 0
                for i in range(len(records)):
                    print(f"{records[i]["备注"]} -{records[i]["金额"]}元")
                    all_money += records[i]["金额"]
                    print(f"总共花了{all_money}元")
        elif option == "3":
            print("正在退出....")
            save_data(records)
            break
        
        elif option == "4":
            today = datetime.now().strftime("%Y-%m-%d")
            total = 0
            count = 0
            for item in records:
                if item.get("日期") == today:
                    total += item["金额"]
                    count += 1
            if count == 0:
                print("今天还没记账哦")
            else:
                print(f"今天记了 {count} 笔，共花了 {total} 元")
        elif option == "5":
             if not records:
                  print("没有记录可删除")
             else:
                  records.pop()
                  save_data(records)
                  print("已删除")     

if __name__ == "__main__":
     main()
         


