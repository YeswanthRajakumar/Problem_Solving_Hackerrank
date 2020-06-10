scores = [10, 5 ,20 ,20 ,4 ,5 ,2 ,25 ,1]
h_score = [scores[0]]
l_score = [scores[0]]
print('scores  : ',scores)
for i in range(len(scores)):
    max_s = scores[i]
    min_s = scores[i]
    if scores[i] > max(h_score):
        h_score.append(max_s)
    elif scores[i] == max(h_score):
         h_score.append(scores[i])

    if scores[i] < min(l_score):
        l_score.append(min_s)

    elif scores[i] < min(l_score):
        l_score.append(scores[i])

print('highest : ',h_score)
print('lowest  : ',l_score)