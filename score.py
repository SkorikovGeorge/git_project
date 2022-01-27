def score(time):
    seconds = int(time) // 1000
    minutes = seconds // 60
    if minutes < 1:
        if seconds >= 10:
            score = f'0:{seconds}'
            return score
        else:
            score = f'0:0{seconds}'
            return score
    else:
        seconds = seconds - minutes * 60
        if seconds >= 10:
            score = f'{minutes}:{seconds}'
            return score
        else:
            score = f'{minutes}:0{seconds}'
            return score


def get_best_result(filename):
    f = open(filename, mode='r')
    line = f.readlines()
    f.close()
    return line[0]


def write_new_best_result(filename, best_score):
    open(filename, mode='w').close()
    f = open(filename, mode='w')
    f.write(best_score)
    f.close()
