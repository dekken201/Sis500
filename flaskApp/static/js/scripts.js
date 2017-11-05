document.getElementById("enviarPerg").addEventListener("click", verifica);
document.getElementById("assuntos").addEventListener("change", setAssunto);

var resp = '';
var top3;
var assunto = '';

function setAssunto() { //Se alterado o select, atribui a var assunto
    assunto = $("#assuntos option:selected").val();
}

$('#txtArea').keypress(function (e) { //Se pressionado enter chama o método
    if (e.keyCode == 13) {
        verifica();
    }
});

function verifica() { //verifica se esta vazio
    var msg = $('#txtArea').val();
    if (assunto != '') {
        if (msg != '') {
            enviar(msg);
        } else {
            alert("Digite uma pergunta!");
        }
    } else {
        alert("Escolha um assunto primeiro!");
    }
}

function enviar(pergunta) {
    getData(pergunta, assunto);
    exibirResp();
}

function getData(pergunta, livro) {
    $.ajax({
        url: '/getData',
        async: false,
        data: {
            "pergunta": pergunta,
            "livro": livro
        },
        type: 'POST',
        success: function (data) {
            top3 = $.parseJSON(data);
            //alert(JSON.stringify(resposta["0"]));
            //alert(JSON.stringify(resposta));
        },
        error: function (error) {
            console.log("Error");
        }
    });
}

function exibirResp() {
    var template = [
        '<div class="cont">',
            '<div class="cmsg" id="cx">',
                '<div class="tit">Pergunta similar:</div>',
                '<div class="resp">{{pergunta}}</div>',
                '<div class="cxresp">',
                    '<div class="tit">Resposta Similar:</div>',
                    '{{resposta}}',
                    '<div class="pag">{{pagina}}</div>',
                '</div>',
            '</div>',
        '</div>'
    ].join("\n");

    for (i = 0; i < 3; i++) {
        var html = Mustache.render(template, top3[i]);
        $("#cxresp").append(html);
    }
}
