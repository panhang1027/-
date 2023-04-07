import os
import re

def take_lines():
    # 输入语料文件
    file_path = os.path.join('nlp_data', 'yaoqiu_data.txt')


    lines = []
    for line in open(file_path, 'r', encoding='utf-8'):
        if len(line) <= 9 or line[5]!='：' or line[6:8] != '1.':
            continue

        # r3 = "[^\u4e00-\u9fa50-9a-zA-Z，。.、:/t“”]+[^-\/ ]"s./
        r3 = "[!//_,$&%^*()<>+\"'?@#{}]+|[——！\\\\=？“”‘’《》【】￥……（）]+"

        line = re.sub(r3, '', line)
        if line in lines:
            continue
        lines.append(line)
    # lines = [line.split('') for line in lines]
    lines = [line + "\n" for line in lines]

    return lines

if __name__ == '__main__':
    lines = take_lines()
    print(lines)
    output_data = open('Pre_yaoqiu.txt','w+',encoding='utf-8')
    output_data.write(''.join('%s' %a for a in lines))
    print('11')
    
