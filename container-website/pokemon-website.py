import ast
from flask import Flask, render_template 
import redis
 
app = Flask(__name__) 


@app.route('/') 
def print_logs():
    try:
        conn = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

        mostCommonType = conn.get("mostCommonType")
        averageHP = conn.get("averageHP")
        weakestAttack = conn.get("weakestAttack")
        strongestAttack = conn.get("strongestAttack")
        toughestPokemonName = conn.get("toughestPokemonName")
        toughestPokemon = conn.get("toughestPokemon")
        
        allPokemon = conn.get("allPokemon")
        allPokemon = ast.literal_eval(allPokemon)
        allPokemon = allPokemon[::-1]

        # For Graph
        allHp = ast.literal_eval(conn.get("allHp"))
        allAttack = ast.literal_eval(conn.get("allAttack"))
        allNames = ast.literal_eval(conn.get("allNames"))

        rollingStatus = conn.get("rollingStatus")
        mostCommonTypeLen = conn.get("mostCommonTypeLen")
        print("Recieved Analytics", flush=True)
    except Exception as ex:
        str(ex)

    return render_template(
        "home.html",
        mostCommonType = mostCommonType,
        averageHP = averageHP,
        weakestAttack = weakestAttack,
        toughestPokemon = toughestPokemon,
        toughestPokemonName = toughestPokemonName,
        strongestAttack = strongestAttack,
        allPokemon = allPokemon,
        listLen = len(allPokemon),
        allHp = allHp,
        allAttack = allAttack,
        allNames = allNames,
        rollingStatus = rollingStatus,
        mostCommonTypeLen = mostCommonTypeLen
    )
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')