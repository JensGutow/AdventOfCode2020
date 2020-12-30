'''
https://adventofcode.com/2020/day/25
--- Day 25: Combo Breaker ---

RFID card <-> door 

"I see! Well, your only other option would be to reverse-engineer the cryptographic handshake 
the card does with the door and then inject your own commands into the data stream, but that's definitely impossible." You thank them for their time.

The handshake used by the card and the door involves an operation that transforms a subject number. 
To transform a subject number, start with the value 1. 
Then, a number of times called the loop size, perform the following steps:

    Set the value to itself multiplied by the subject number.
    Set the value to the remainder after dividing the value by 20201227.

The card always uses a specific, secret loop size when it transforms a subject number. The door always uses a different, secret loop size.

The cryptographic handshake works like this:

    The card transforms the subject number of 7(unbekannt?) according to the card's secret loop size. The result is called the card's public key.
    The door transforms the subject number of 7 according to the door's secret loop size. The result is called the door's public key.
    The card and door use the wireless RFID signal to transmit the two public keys (your puzzle input) to the other device. 
    Now, the card has the door's public key, and the door has the card's public key. Because you can eavesdrop on the signal, 
    you have both public keys, but neither device's loop size.
    The card transforms the subject number of the door's public key according to the card's loop size. The result is the encryption key.
    The door transforms the subject number of the card's public key according to the door's loop size. The result is the same encryption key as the card calculated.

If you can use the two public keys to determine each device's loop size, you will have enough information to calculate the secret encryption key 
that the card and door use to communicate; this would let you send the unlock command directly to the door!

For example, suppose you know that the card's public key is 5764801. With a little trial and error, 
you can work out that the card's loop size must be 8, because transforming the initial subject number of 7 with a loop size of 8 produces 5764801.

Then, suppose you know that the door's public key is 17807724. By the same process, 
you can determine that the door's loop size is 11, because transforming the initial subject number of 7 with a loop size of 11 produces 17807724.

At this point, you can use either device's loop size with the other device's public key to calculate the encryption key. 
Transforming the subject number of 17807724 (the door's public key) with a loop size of 8 (the card's loop size) 
produces the encryption key, 14897079. (Transforming the subject number of 5764801 (the card's public key)
 with a loop size of 11 (the door's loop size) produces the same encryption key: 14897079.)

What encryption key is the handshake trying to establish?

##################################
# Textanalyse / Ideen und lösung
##################################

handshake door <-> card
    transform(subjectNr, loop_size)
    loop_size: für door und carte ein Geheimnnis, verschiedne
crypt-handshake:
    card: transform subj_nr 7 mal (cards secret loop size) -> cards cards public key
    door: transfomr subj_nr 7 mal (doors secret loop size) -> doors public key
    puzzle input = two public key (for card and door)
    Austausch der public keys zwischen door / card: LOOP_SIZEs für card/door sind unbekannt
    subject: für Card ist das der public key von der Tür (und umgekert)
    card: transform(public_key_door, loop_size_card) -> enc_Key_card
    door: transfomr(public_key_card, loop_size_door) -> enc_key_door
        -> enc_key_card == enc_key_dor
    
'''

def read_input(file_name):
    with open(file_name, 'r') as f:
        return int(f.readline().strip()), int(f.readline().strip())


def transform(subj, loop_size, expected=None):
    val = 1
    for i in range(loop_size):
        val *= subj
        val %= 20201227
        if val == expected:
            return i + 1  # because range() starts at 0
    return val if expected is None else None


def bruteforce(keys, max_loop_size=100_000_000):
    return tuple(transform(7, max_loop_size, pub) for pub in keys)


if __name__ == '__main__':
    pub = read_input("tag_25.txt")
    print('Brute-forcing keys...')
    prv = bruteforce(pub)
    print('Private keys are: {0}'.format(prv))
    print('Calculating encryption key...')
    print('The encryption key is: {0}'.format(
        transform(pub[0], prv[1])))