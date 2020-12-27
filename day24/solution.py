tiles = set()

def repl(line):
    return line.strip().replace("ne", "a").replace("se", "b").replace("sw","c").replace("nw", 'd')

newlines = [repl(line) for line in open("input")]
moves = {'a':(-1,1), 'e':(0,1), 'b':(1,0), 'c':(1,-1), 'w':(0,-1), 'd':(-1,0)}

def tiletoflip(directions):
    tile = (0,0)
    for direction in directions:
        tile = tuple([a1 + a2 for a1, a2 in zip(tile, moves[direction])])
    return tile

for line in newlines:
    tile = (0,0)
    for direction in line:
        tile = tuple([a1 + a2 for a1, a2 in zip(tile, moves[direction])])
    if tile in tiles:
        tiles.remove(tile)
    else:
        tiles.add(tile)

print("part 1", len(tiles))

def adjtiles(tile):
    tiles = set()
    for move in moves.values():
        tiles.add(tuple([a1 + a2 for a1, a2 in zip(tile, move)]))
    return tiles

for days in range(100):
    newtiles = set()
    for blacktile in tiles:
        if 0 < len(adjtiles(blacktile).intersection(tiles)) < 3:
            newtiles.add(blacktile)
        for adjtile in adjtiles(blacktile):
            if adjtile not in tiles:
                whitetile = adjtile
                if len(adjtiles(whitetile).intersection(tiles)) == 2:
                    newtiles.add(whitetile)
    tiles = newtiles
    
print("Part 2",len(newtiles))
