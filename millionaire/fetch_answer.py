import random


class Fetcher:
    def __init__(self, filepath):
        self.filepath = filepath

        self.key = {}
        self.divider_small = '@@@@'
        self.divider_big = '\n####'

        file = open(self.filepath, mode='r', encoding='cp1252')

        data = file.read().encode("cp1252", errors='replace').decode('cp1252')
        qas = data.split(self.divider_big)

        for qa in qas:
            if len(qa) == 0:
                continue
            q,a = qa.split(self.divider_small)
            self.key[q] = a

        file.close()

    # returns answerindex (int), guessed (boolean)
    def check(self, question, answers, indices=[0,1,2,3]):
        qhash = self.questionhash(question, answers)
        if qhash in self.key:
            ans = self.key[qhash]
            return (answers.index(ans), False)
        else:
            print(qhash)
            return (random.choice(indices), True)

    # make it so each question and set of answers has a unique hash
    def questionhash(self, question, answers):
        a = answers[:]
        a.sort()
        return (question + ''.join(a)).encode("cp1252", errors='replace').decode("cp1252")

    # adds q/a to txt file
    def addanswer(self, question, answers, correctindex):
        qhash = self.questionhash(question, answers)
        ans = answers[correctindex]

        # update dict and file
        self.key[qhash] = ans
        file = open(self.filepath, mode='a', encoding='cp1252')
        file.write(self.divider_big + qhash + self.divider_small + ans)
        file.close()


def convert(big_new, small_new):
    f = Fetcher('answers.txt')
    k = f.key
    file = open(f.filepath, mode='w+')
    for i,question in enumerate(k):
        if i > 0:
            file.write(big_new)
        file.write(question + small_new + k[question])
    file.close()


if __name__ == '__main__':
    convert('\n####','@@@@')