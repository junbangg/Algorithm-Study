# code divided by steps
def solution(new_id):
    #1
    new_id = new_id.lower()
    #2
    new_id = ''.join((filter(lambda x: x in ['-', '_', '.'] or x.isalpha() or x.isnumeric(), new_id)))
    #3
    for i in range(len(new_id)-1):
        if new_id[i] == new_id[i+1] == '.':
            new_id = new_id[:i] + '*' + new_id[i+1:]
    new_id = ''.join((filter(lambda x:x != '*', new_id)))
    #4
    if new_id.startswith('.'): new_id = new_id[1:]
    if new_id.endswith('.'): new_id = new_id[:-1]
    #5
    if new_id == '': new_id = 'a'
    #6
    if len(new_id) >= 16: new_id = new_id[:15]
    if new_id.endswith('.'): new_id = new_id[:-1]
    #7
    if len(new_id) <= 2:
        last = new_id[len(new_id)-1]
        while len(new_id) < 3:
            new_id += last
    return new_id
