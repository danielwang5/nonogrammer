import random


class Fetcher:
    def __init__(self, filepath):
        self.filepath = filepath

        self.key = {}
        self.divider_small = '####'
        self.divider_big = '@@@@'

        file = open(self.filepath, mode='r')

        data = file.read()
        qas = data.split(self.divider_big)

        for qa in qas:
            if len(qa) == 0:
                continue
            q,a = qa.split(self.divider_small)
            self.key[q] = a

        file.close()

    # returns answerindex (int), guessed (boolean)
    def check(self, question, answers):
        qhash = self.questionhash(question, answers)
        if qhash in self.key:
            ans = self.key[qhash]
            return (answers.index(ans), False)
        else:
            return (random.randint(0,3), True)

    # make it so each question and set of answers has a unique hash
    def questionhash(self, question, answers):
        a = answers[:]
        a.sort()
        return question + ''.join(a)

    # adds q/a to txt file
    def addanswer(self, question, answers, correctindex):
        qhash = self.questionhash(question, answers)
        ans = answers[correctindex]

        # update dict and file
        self.key[qhash] = ans
        file = open(self.filepath, mode='a')
        file.write(self.divider_big + qhash + self.divider_small + ans)
        file.close()