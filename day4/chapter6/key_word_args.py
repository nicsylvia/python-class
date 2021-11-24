def states_capital(**key_word_args):
    print(key_word_args)

states_capital(imo='Owerri', Abia ='Umuahia', Adamawa ='Yola')

def states_capital(**key_word_args):
    for state, capital in key_word_args.items():
        print(f'{state} <====> {capital} ')

states_capital(Imo='Owerri', Abia ='Umuahia', Adamawa ='Yola')