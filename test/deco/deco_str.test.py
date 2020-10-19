from texting import bracket

from pyspare.deco.deco_str import deco_str

candidates = {
    'Modigliani': 'What is the "cost of capital" to a, firm in a world in which funds are used to acquire assets whose yields are uncertain; and in which capital can be obtained by many different media, ranging from pure debt instruments, representing money-fixed claims, to pure equity issues, giving holders only the right to a pro-rata share in the uncertain venture? This question has vexed at least three classes of economists: \n(1) the corporation finance specialist concerned with the techniques of financing firms so as to ensure their survival and growth; \n(2) the managerial economist concerned with capital budgeting; and \n(3) the economic theorist concerned with explaining investment behavior at both the micro and macro levels.',
}


def test():
    for key, text in candidates.items():
        print(bracket(key), deco_str(text, first_line_indent=len(key) + 3))


test()
