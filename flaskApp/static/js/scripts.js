document.write('<script type="text/javascript" src="../static/js/mustache.min.js"></script>')
document.getElementById("enviarPerg").addEventListener("click", verifica);
document.getElementById("assuntos").addEventListener("change", setAssunto);


var resp = '';
var top3;
var assunto = '';
var limpo = true;

function setAssunto() { //Se alterado o select, atribui a var assunto
    clean();
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
            clean();
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
        },
        error: function (error) {
            console.log("Error");
        }
    });
}

function exibirResp() {
    var template = [
        '<div class="cont" id="cx">',
            '<div class="cmsg">',
                '<div class="tit">Pergunta similar:</div>',
                '<div class="resp">{{pergunta}}</div>',
                '<div class="cxresp">',
                    '<div class="tit">Resposta Similar:</div>',
                    '{{resposta}}',
                    '<div class="pag">Página(s) no livro: {{pagina}} - Proximidade: {{ratio}}%</div>',
                '</div>',
            '</div>',
        '</div>'
    ].join("\n");
    var x;
    for (x in top3) {
        var html = Mustache.render(template, top3[x]);
        $("#cxresp").append(html);
    }
    limpo = false;
}

function clean() {
    if (!limpo) {
        for (var a in top3) {
            $("#cx").remove();
        }
        limpo = true;
    }
}

//Teste unitário, método para popular informações:
//document.write('<script src="../static/js/test.js"></script>');$(document).ready(function () {var tm = popular();top3 = tm;exibirResp();});
