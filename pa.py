with open ('top_50_2023.csv', 'r') as csvfile:
    header = next(csvfile)
    print(header)
    data = []
    for line in csvfile:
        line = line[:-1].split(',')
        data.append(line)

    import csv

    with open('top_50_2023.csv', 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        rows = []
        header = next(csvfile)
        for row in csv_reader:
            rows.append(row)

    import ast
    GENRE = 4
    for row in rows:
        row[GENRE] = ast.literal_eval(row[GENRE])
    print(rows[0])


    def is_valid(num: str) -> bool:
        try:
            float(num)
            if 0 < num < 1:
                return True
        except ValueError:
            return False
    # danceability = 5
    # sum_dance = 0
    # counter = 0
    # for row in rows:
    #     if is_valid(row(danceability)):
    #         counter += 1
    #         sum_dance += float(row[danceability])
    # print('average', sum_dance/counter)

    EXPLICIT = 2
    count_2 = 0

    for row in rows:
        if row[EXPLICIT] == 'True':
            count_2 += 1
    print('explicit', count_2)

    GENRES = 4
    genres_count = {}
    for row in rows:
        for genre in row[GENRES]:
            if genre in genres_count:
                genres_count[genre] += 1
            else:
                genres_count[genre] = 1

    top_3 = sorted(genres_count.items(), key=lambda x: x[1], reverse=True)[:3]
    print(top_3)

    #The most popular year
    YEAR = 3
    years = {}
    for row in rows:
        date = row[YEAR]
        year = date.split('-')[0]
        if year in years:
            years[year] += 1
        else:
            years[year] = 1

    top_year = sorted(years.items(), key=lambda x: x[1], reverse=True)[:1]
    print(top_year)

   # Average Liveliness with Energy Criteria

    LIVELINESS = 11
    ENERGY =  7
    sum_live = 0
    counter_2 = 0
    for row in rows:
        if float(row[ENERGY]) > 0.5:
            counter_2 += 1
            sum_live += float(row[LIVELINESS])
    print('average', sum_live/counter_2)

    #The most popular artist
    ARTISTS = 0
    artists_count = {}
    for row in rows:
        artist = row[ARTISTS]
        if artist in artists_count:
            artists_count[artist] += 1
        else:
            artists_count[artist] = 1

    top_artist = sorted(artists_count.items(), key=lambda x: x[1], reverse=True)[:1]
    print(top_artist)




