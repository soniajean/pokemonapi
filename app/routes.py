
from app import app

from flask import render_template, request, url_for, redirect

from .forms import SignUpForm
from .models import User
from .forms import PokemonForm
import requests, json

def getPokemon(pokemon):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon}'
    response = requests.get(url)
    if response.ok:
        my_dict = response.json()
        pokemon_dict = {}
        pokemon_dict["Name"] = my_dict["name"]
        pokemon_dict["Ability"] = my_dict["abilities"][0]["ability"]["name"]
        pokemon_dict["Base XP"] = my_dict["base_experience"]
        pokemon_dict["Front Shiny"] = my_dict["sprites"]["front_shiny"]
        pokemon_dict["Base ATK"] = my_dict["stats"][1]["base_stat"]
        pokemon_dict["Base HP"] = my_dict["stats"][0]["base_stat"]
        pokemon_dict["Base DEF"] = my_dict["stats"][2]["base_stat"]

        
        return pokemon_dict

@app.route('/')
def homePage():
    teachers = [
        {
        'name': 'Brendan',
        'age': 456,
        'spec' : 'Vim'
        },
        {
        'name': 'Rachel',
        'age' : 342,
        'spec' : 'student relations'
        },
        {
        'name' : 'Brandt',
        'age' : 567,
        'spec': 'none'
        }
    ]
    fav_animal = 'Tiger'
    return render_template('index.html', teachers=teachers, f = fav_animal)

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/register', methods=["GET", "POST"])
def registerPage():
    form = SignUpForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)


            user = User(username, email, password)            
            user.saveUser()
            return redirect(url_for('loginPage'))

    return render_template('register.html', form=form)

@app.route('/pokemon_search', methods=["GET", "POST"])
def findpokemon():
    form = PokemonForm()
    if request.method == 'POST':
         if form.validate():  
            data = getPokemon(pokemon)    
            pokemon = form.pokemon.data
            print(pokemon)
           
    return render_template('pokemon_search.html', form=form)
    
    findpokemon('pikachu')

@app.route('/pokemon_display', methods=["GET", "POST"])
def displaypokemon():
    form = PokemonForm()
    if request.method == 'POST':
         if form.validate():  
            data = getPokemon(pokemon)    
            pokemon = form.pokemon.data
            print(pokemon)
           
    
    return render_template('pokemon_display.html', form=form)
   
    findpokemon('pikachu')
