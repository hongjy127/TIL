from app_base import Application

# 실제로는 최적화된 라이브러리가 있어서 그걸 상속함
class DiaryApp(Application):
    def __init__(self):
        super().__init__()

    def create_menu(self, menu):
        menu.add('쓰기', self.write_today)
        menu.add('수정', self.update)
        menu.add('삭제', self.delete)
        menu.add('종료', self.exit)
        pass

    def write_today(self):
        print('오늘 일기 쓰기')

    def update(self):
        print('일기 수정')

    def delete(self):
        print('일기 삭제')


def main():
    app = DiaryApp()
    app.run()

main()

