import moviepy.editor as mp
import argparse

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--src')
    parser.add_argument("--begin", default=0)
    parser.add_argument("--end", default=1)
    parser.add_argument("--output", default='output_video.mp4')

    parser_args = parser.parse_args()
    source_file = parser_args.src

    video = mp.VideoFileClip(source_file)

    begin = parser_args.begin
    end = parser_args.end
    output_file = parser_args.output

    if float(begin) > video.duration or float(begin) < 0:
        print('Wrong argument begin!')
        print('Parametr --begin set to default - 0')
        begin = 0

    if float(end) > video.duration or float(end) < 1:
        print('Wrong argument end!')
        print('Parametr --end set to default - 1')
        end = 1

    sub_video = video.subclip(begin, end)
    sub_video.write_videofile(output_file)

main()