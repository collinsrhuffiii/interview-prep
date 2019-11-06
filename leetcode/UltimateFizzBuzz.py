def fb(n, shout_match):
    fb_str = ''.join(shout if n % match == 0 else '' for shout, match in shout_match)
    if not fb_str:
        fb_str = int(n)
    return fb_str

shout_match_pair = [('Fizz', 3), ('Buzz', 5), ('Bazz', 7)]
for i in range(1, 101):
    print(fb(i, shout_match_pair))
