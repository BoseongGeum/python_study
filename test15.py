def solution(genres, plays):
    answer = []
    genres_plays = {}
    
    for i in range(len(genres)):
        if genres[i] in genres_plays:
            genres_plays[genres[i]][0] += plays[i]
            if genres_plays[genres[i]][1][1] < plays[i]:
                genres_plays[genres[i]][2] = genres_plays[genres[i]][1]
                genres_plays[genres[i]][1] = (i, plays[i])
            elif genres_plays[genres[i]][2][1] < plays[i]:
                genres_plays[genres[i]][2] = (i, plays[i])
        else:
            genres_plays[genres[i]] = [plays[i], (i, plays[i]), (-1, 0)]
            
    sorted_genres = sorted(genres_plays, key=lambda x: genres_plays[x][0])[::-1]
    
    for g in sorted_genres:
        answer.append(genres_plays[g][1][0])
        if genres_plays[g][2][0] != -1:
            answer.append(genres_plays[g][2][0])
    
    return answer
