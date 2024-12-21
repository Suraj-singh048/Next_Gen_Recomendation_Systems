import ollama
from flask import Flask, request, jsonify

def get_llama_response(content):
    stream = ollama.chat(
        model='llama3.2',
        messages=[{'role': 'user', 'content': content }],
        stream=True,
    )
    
    return ''.join([chunk['message']['content'] for chunk in stream])

app = Flask(__name__)

@app.route('/api/llama-chatbot', methods=['GET'])
def llama_chatbot_handler():
    args = request.args
    query = args.get('query', type=str, default=None)
    
    if not query:
        return jsonify({
            'message': 'Please provide a query to respond',
            'error': True
        })
        
    res = get_llama_response(query)
    return jsonify({
        'message': 'Response generated',
        'response': res,
        'error': False 
    })
    
if __name__ == '__main__':
    app.run(debug=True)