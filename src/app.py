from flask import Flask, jsonify, request  #esto importa Flask para crear el servidor
                    #esto importa el método jsonify
app = Flask(__name__)  

todos = [  #esto es una lista (array en JS)              (una lista)     (diccionario)
    {"label": "My first task", "done": False}]  #esto es un array con un objeto dentro
    

                   #esto es un endpoint
@app.route("/todos", methods=["GET"])  #esto crea la ruta del servidor
def hello_world():              
    json_text = jsonify(todos)  #esto convierte el texto en formato json y es una variable
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json #esto guarda en la variable request_body 
    todos.append(request_body) #esto es como el .push de los arrays de JS. Agrega el request body
    print("Incoming request with the following body", request_body)        #a la lista to-do 
    return jsonify(todos)

                #lo que va entre <> guarda en una varible(en este caso position) esa parte de la URL
                #int es para convertir a integer (un número entero, no decimales)
@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    todos.pop(position) #esto elimina una posición concreta en la lista. 
    #para eliminar un item concreto, se usa .remove
    print("This is the position to delete:", position)
    return jsonify(todos)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3245, debug=True)  #esto hace que el servidor funcione

