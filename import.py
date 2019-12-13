import csv
from comedia.models import Video



f = open('videos.txt', 'r')
for line in f:
    line = line.rstrip('\n').split(',')
    print(line)
    video = Video()
    video.name = line[0]
    video.url = line[1]
    video.tipo = line[2]
    video.save()

f.close()


if __name__ == '__main__':
    insertar()
