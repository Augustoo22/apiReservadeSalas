const API_URL = 'http://example.com/api/salas';

function listarSalas() {
    fetch(API_URL)
        .then(response => response.json())
        .then(data => {
            const listaSalas = document.getElementById('salas-lista');
            listaSalas.innerHTML = '';
            data.forEach(sala => {
                const item = document.createElement('li');
                item.classList.add('sala-item');
                item.innerHTML = `<h3>${sala.nome}</h3><p>Capacidade: ${sala.capacidade}</p>`;
                listaSalas.appendChild(item);
            });
        })
        .catch(error => console.error('Erro ao listar salas:', error));
}

function detalhesSala() {
    const salaId = document.getElementById('sala-id').value;
    fetch(`${API_URL}/${salaId}`)
        .then(response => response.json())
        .then(data => {
            const detalhesSala = document.getElementById('detalhes');
            detalhesSala.innerHTML = `<h3>${data.nome}</h3><p>Capacidade: ${data.capacidade}</p><p>Localização: ${data.localizacao}</p>`;
            document.getElementById('detalhes-sala').style.display = 'block';
        })
        .catch(error => console.error('Erro ao obter detalhes da sala:', error));
}
