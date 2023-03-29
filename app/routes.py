
from app import app

from flask import render_template, request, url_for, redirect
from flask_login import current_user, login_user, logout_user

from .auth.forms import SignUpForm, LoginForm, ProfileForm
from .models import User, Pokemon
from .auth.forms import PokemonForm
from .services import getPokemon
import requests, json

@app.route('/')
def homePage():
    Pokey = [
    ]
    fav_animal = 'Poke'
    return render_template('index.html', pokey=Pokey, f = fav_animal)

@app.route('/login')
def loginPage():
    return render_template('login.html')


@app.route('/signUp', methods=["GET", "POST"])
def signUpPage():
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

    return render_template('signUp.html', form=form)

@app.route('/editProfile', methods=["GET", "POST"])
def ProfilePage():
    form = ProfileForm()
    if request.method == 'POST':
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data
            print(username, email, password)


            user = User(username, email, password)            
            user.saveUser()
            return redirect(url_for('loginPage'))

    return render_template('ProfilePage.html', form=form)



@app.route('/pokemon_search', methods=["GET", "POST"])
def findpokemon():
    form = PokemonForm()
    if request.method == 'POST':
        if form.validate():  
            pokemon = form.pokemon.data
            pokedict = Pokemon.query.filter_by(name=pokemon).first()
            if pokedict:
                print(f'From Query')
                return render_template('pokemon_search.html', form=form, pokedict=pokedict)
            

            getpoke= getPokemon(pokemon)
            name = getpoke['name']
            ability = getpoke['ability']
            base_xp = getpoke['base_xp']
            front_shiny = getpoke['front_shiny']
            base_atk = getpoke['base_atk']
            base_hp = getpoke['base_hp' ]
            base_def = getpoke['base_def']

            pokedict = Pokemon(name, ability, base_xp, front_shiny, base_atk, base_hp, base_def) 
            print(f'From API call')
            pokedict.savePokemon()            
            return render_template('pokemon_search.html', form=form, pokedict=pokedict)

    return render_template('pokemon_search.html', form=form)
