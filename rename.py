import os

path = 'D:/Git/5f/data/old_morning/'
f = []
for (dirpath, dirnames, filenames) in os.walk(path):
    f.extend(filenames)
    break

f = [f'{path}{x}' for x in f]
print(f)

i = 0
for v in f:
    if v.endswith('jpeg') or v.endswith('jpg') or v.endswith('png'):
        while True:
            try:
                os.rename(v, f'{path}{i}.jpg')
                break
            except FileExistsError:
                i += 1
        i += 1
    elif v.endswith('gif'):
        os.remove(v)
    else:
        print('unknown image', v)