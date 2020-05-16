from collections import defaultdict


def solution(genres, plays):
    answer = []
    musics = defaultdict(list)
    genreMax = defaultdict(int)

    for i in range(len(genres)):
        musics[genres[i]].append( (i, plays[i]) )
        # 가장 노래가 많이 재생된 장르를 알기 위해 계속 더함
        genreMax[genres[i]] += plays[i]

    # 횟수 합으로 내림차순 정렬
    genreMax = sorted(genreMax.items(), key = lambda x : x[1], reverse=True)

    for genre, _ in genreMax :

        music_list =  musics[genre]
        # 횟수 합으로 내림차순, id값으로 오름차순 정렬
        music_list = sorted(music_list, key = lambda x : (x[1],-x[0]) , reverse=True)

        # 장르 노래가 최대 2개만 넣기.
        cnt = 0
        for music in music_list :
            if cnt > 1 :
                break
            else :
                answer.append(music[0])
            cnt += 1


    return answer


print(solution(['classic', 'pop', 'classic', 'classic', 'pop'], [500, 600, 150, 800, 2500]))