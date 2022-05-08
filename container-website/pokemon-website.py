import ast
from flask import Flask, render_template 
import redis
 
app = Flask(__name__) 


@app.route('/') 
def print_logs():
    try:
        conn = redis.StrictRedis(host='redis', port=6379, decode_responses=True)

        # Pokemon
        mostCommonType = conn.get("mostCommonType")
        averageHP = conn.get("averageHP")
        weakestAttack = conn.get("weakestAttack")
        strongestAttack = conn.get("strongestAttack")
        toughestPokemonName = conn.get("toughestPokemonName")
        toughestPokemon = conn.get("toughestPokemon")
        
        allPokemon = conn.get("allPokemon")
        allPokemon = ast.literal_eval(allPokemon)
        allPokemon = allPokemon[::-1]

        rollingStatus = conn.get("rollingStatus")
        mostCommonTypeLen = conn.get("mostCommonTypeLen")
        print("Recieved Pokemon Analytics", flush=True)

        # Digimon Metrics
        D_averageHP = conn.get("D_averageHP")
        D_weakestAttack = conn.get("D_weakestAttack")
        D_strongestAttack = conn.get("D_strongestAttack")
        D_toughestPokemonName = conn.get("D_toughestPokemonName")
        D_toughestPokemon = conn.get("D_toughestPokemon")
        
        # For Graph
        allHp = ast.literal_eval(conn.get("allHp"))
        allAttack = ast.literal_eval(conn.get("allAttack"))
        allNames = ast.literal_eval(conn.get("allNames"))
        D_allHp = ast.literal_eval(conn.get("D_allHp"))
        D_allAttack = ast.literal_eval(conn.get("D_allAttack"))
        D_allNames = ast.literal_eval(conn.get("D_allNames"))
        
        print(len(D_allNames), flush=True)

        # Combine Data
        allHp = allHp + D_allHp
        allAttack = allAttack + D_allAttack
        allNames = allNames + D_allNames
        
        print("Recieved Digimon Analytics", flush=True)
        
        # Unused Digimon Data
            # D_mostCommonType = conn.get("D_mostCommonType")
            # D_rollingStatus = conn.get("rollingStatus")
            # D_mostCommonTypeLen = conn.get("mostCommonTypeLen")
            # D_allPokemon = conn.get("D_allPokemon")
            # D_allPokemon = ast.literal_eval(D_allPokemon)
            # D_allPokemon = D_allPokemon[::-1]
        

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
        mostCommonTypeLen = mostCommonTypeLen,
        D_averageHP = D_averageHP,
        D_weakestAttack = D_weakestAttack,
        D_strongestAttack = D_strongestAttack,
        D_toughestPokemonName = D_toughestPokemonName,
        D_toughestPokemon = D_toughestPokemon
    )
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')