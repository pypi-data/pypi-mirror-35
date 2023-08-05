from sample_app.package_one.pack_one import PackOne, NyT
from sample_app.package_two.pack_two import PackTwo


def main():
    p1 = PackOne()
    p2 = PackTwo()
    p3=NyT()

    p1.do()
    p2.process()
    p3.news()


if __name__ == '__main__':
    main()
