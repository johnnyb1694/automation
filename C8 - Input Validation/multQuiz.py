
import pyinputplus as pyip
import random
import time

num_questions = 10
correct_answers = 0

for q in range(num_questions):
    n1 = random.randint(1, 12)
    n2 = random.randint(1, 12)

    prompt = '%s: %s x %s = ...' % (q, n1, n2)

    try:
        pyip.inputStr(prompt,
                      allowRegexes=['^%s$' % (n1 * n2)],
                      blockRegexes=[('.*', 'Incorrect!')],
                      timeout=8,
                      limit=3)
    except pyip.TimeoutException:
        print('Out of time!')
    except pyip.RetryLimitException:
        print('Out of tries!')
    else:
        print('Correct!')
        correct_answers += 1
        time.sleep(1)
    print('Score: %s / %s' % (correct_answers, num_questions))
