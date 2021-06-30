class Book:
    def __init__(self,name , author , comment , state = 0):
        self.name = name
        self.author = author
        self.comment = comment
        self.state = state

    def __str__(self):
        if self.state == 0:
            # 如果属性state等于0
            status = '未借出'
            # 将字符串'未借出'赋值给status
        else:
            status = '已借出'
        return '名称：《%s》 作者：%s 推荐语：%s\n状态：%s ' % (self.name, self.author, self.comment, status)
        # 返回书籍信息

class BookManager:

    books = []

    def __init__(self):
        book1 = Book('惶然录','费尔南多·佩索阿','一个迷失方向且濒于崩溃的灵魂的自我启示，一首对默默无闻、失败、智慧、困难和沉默的赞美诗。')
        book2 = Book('以箭为翅','简媜','调和空灵文风与禅宗境界，刻画人间之缘起缘灭。像一条柔韧的绳子，情这个字，不知勒痛多少人的心肉。')
        book3 = Book('心是孤独的猎手','卡森·麦卡勒斯','我们渴望倾诉，却从未倾听。女孩、黑人、哑巴、醉鬼、鳏夫的孤独形态各异，却从未退场。', 1)
        self.books.append(book1)
        self.books.append(book2)
        self.books.append(book3)


    def menu(self):
        print('欢迎使用流浪图书管理系统，每本沉默的好书都是一座流浪的岛屿，希望你有缘发现并着陆，为精神家园找到一片栖息地。\n')
        while True:
            print('1.查询所有书籍\n2.添加书籍\n3.借阅书籍\n4.归还书籍\n5.退出系统\n')
            choice = int(input('请输入数字选择对应的功能：'))
            if choice == 1:
                self.show_all_book()
                # 调用对象方法时self不能忘
            elif choice == 2:
                self.add_book()
            elif choice == 3:
                self.lend_book()
            elif choice == 4:
                self.return_book()
            elif choice == 5:
                print('感谢使用！愿你我成为爱书之人，在茫茫书海里相遇。')
                break

    def show_all_book(self):
        print(self.books)
        for a in self.books:
        # self是实例对象的替身
            print(a)

    def add_book(self):
        new_name = input('请输入书籍名称：')
        new_author = input('请输入作者:')
        new_commnet = input('请输入寄语:')
        newbooks = Book(new_name,new_author,new_commnet,0)
        self.books.append(newbooks)
        print('书籍录入成功！\n')

    def lend_book(self):
        whichbook = input('你需要什么书：')
        for a in self.books:
            if a.name == whichbook:
                print(True)
            #bookstatus = self.books(whichbook)
                if a.state == 0:
                    print('这本书在库')
                    break
                else:
                    print('已借出')
                    break
            else:
                print('库存没有这本书')
                break

manager = BookManager()
manager.menu()