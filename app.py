import streamlit as st
import requests
import time

with st.form("PokemonInfoForm", clear_on_submit=True):
    st.subheader("Pokémon Info App")

    pokemon_name_or_id = st.text_input("Zadejte jméno nebo ID Pokémona:")
    submit_button =  st.form_submit_button("Získat informace o Pokémonech")

    if submit_button:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id}"
        response = requests.get(url)
        print(response)

        if response.status_code == 200:
            pokemon_data = response.json()
            
            if 'sprites' in pokemon_data and pokemon_data['sprites'] and 'front_default' in pokemon_data['sprites']:
                st.image(pokemon_data['sprites']['front_default'], width=200)

            if 'name' in pokemon_data:
                st.write(f"Name: {pokemon_data['name']}")
            else:
                info_notification = st.info('Zadejte prosím jméno nebo ID Pokémona')
                time.sleep(2)
                info_notification.empty()
            if 'types' in pokemon_data:
                type_pokemon = [t['type']['name'] for t in pokemon_data.get('types', [])]
                st.write(f"Type(s): {', '.join(type_pokemon)}")
        else:
            warning_notification = st.warning('Pokémon nebyl nalezen')
            time.sleep(2)
            warning_notification.empty()