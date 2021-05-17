#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

def main():
    game = [ 'Rock', 'Paper', 'Scissors', 'Lizard', 'Spock' ]
    print(game[1:3])
    print(game[1:5:2])
    print(game.index('Paper'))
    game.append("Computer")
    game.insert(0, "Soccer")
    game.remove("Soccer") 
    game.pop() # remove the last item if none
    del game[0] # remove the first item    
    # can be a sequence as well 

    print_list(game)



def print_list(o):
    for i in o: print(i, end=' ', flush=True)
    print()

if __name__ == '__main__': main()
