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
        toughestPokemonName = conn.get("toughestPokemonName")
        toughestPokemon = conn.get("toughestPokemon")
    except Exception as ex:
        str(ex)

    return render_template("home.html", mostCommonType = mostCommonType, averageHP = averageHP, weakestAttack = weakestAttack, toughestPokemon = toughestPokemon, toughestPokemonName = toughestPokemonName)
   
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')