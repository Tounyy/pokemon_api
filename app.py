import streamlit as st
from classes.poke_api import PokeAPI

poke_api = PokeAPI()
total_pokemon = poke_api.get_total_pokemon_count()

with st.form("PokemonInfoForm"):
    st.subheader("Pokémon Info App")

    pokemon_list = poke_api.get_pokemon_list(limit=total_pokemon)
    pokemon_names_ids = [f"ID {pokemon['url'].split('/')[-2]} - {pokemon['name']}" for pokemon in pokemon_list]

    selected_pokemon = st.selectbox("Vyberte pokémona:", pokemon_names_ids)
    selected_pokemon_id = selected_pokemon.split("ID ")[1].split(" -")[0]

    submit_button = st.form_submit_button("Získat informace o Pokémonech")

    if submit_button:
        pokemon_data = poke_api.get_pokemon_details(selected_pokemon_id)

        if pokemon_data:
            if 'sprites' in pokemon_data and pokemon_data['sprites'] and 'front_default' in pokemon_data['sprites']:
                st.image(pokemon_data['sprites']['front_default'], width=200)

            if 'name' in pokemon_data:
                st.write(f"Name: {pokemon_data['name']}")

            if 'types' in pokemon_data:
                type_pokemon = [t['type']['name'] for t in pokemon_data.get('types', [])]
                st.write(f"Type: {', '.join(type_pokemon)}")
        else:
            st.warning('Pokémon nebyl nalezen')