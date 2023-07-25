from get_code import codigo

codigo_html = codigo


#HTML DO ENVIO DO EMAIL COM O CODIGO ATRIBUIDO NA VAR codigo_html

conteudo_html = f"""<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap');
        h1 {{
            font-size: 24px;
            font-family: 'Inter', sans-serif;
        }}
        h2 {{
            background-color: rgb(13, 0, 202);
            display: inline-block;
            padding: 5px 10px;
            color: aliceblue;
            margin: auto;
            border: 4px solid black;
            border-radius: 10px;
            font-family: 'Inter', sans-serif;
        }}
        h3 {{
            font-family: 'Inter', sans-serif;
        }}
    </style>
</head>
<body>
    <h1>Aqui está seu código de confirmação!</h1>
    <h2>{codigo_html}</h2>
    <h3>Copie o código e cole no programa.</h3>
</body>
</html>
"""
