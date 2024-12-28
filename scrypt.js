function startPrediction() {
    alert("A previsão foi iniciada! Vamos calcular os próximos resultados da roleta.");
}

// Enviar o formulário de contato
document.getElementById('contact-form').addEventListener('submit', function(e) {
    e.preventDefault(); // Impede o envio tradicional do formulário

    // Coletando dados do formulário
    const name = document.getElementById('name').value;
    const email = document.getElementById('email').value;
    const message = document.getElementById('message').value;

    // Exibindo os dados no console (você pode salvar ou enviar para um servidor)
    console.log(`Nome: ${name}`);
    console.log(`E-mail: ${email}`);
    console.log(`Mensagem: ${message}`);

    // Limpando o formulário
    document.getElementById('contact-form').reset();

    // Exibindo uma mensagem de confirmação
    alert("Sua mensagem foi enviada com sucesso! Obrigado pelo seu contato.");
});
