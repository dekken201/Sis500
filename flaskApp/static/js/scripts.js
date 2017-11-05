
    $('#txtArea').keypress(function(e) {
        if (e.keyCode == 13) {
            gravar();
        }
    });
    var anim = "<div class='animated zoomIn'>";
    var divChat = $("#cx"); //puxa o div da caixa de msg
    var resp = '';
    var top3;

    function gravar() {
        var msg = $('#txtArea').val(); // puxa o texto do input - acredito que possa enviar para o bot apartir dessa variável
        if (msg != '') {
            var divUsuario = anim + "<div class='chat usuario'><br><div class='foto'><img src='{{ url_for('static', filename = 'img/usr.png') }}'></div><br><div class='mensagem'>" + msg + "</div><br></div></div>"
            divChat.append(divUsuario); //coloca a mensagem na div da caixa
            $('#txtArea').val(''); // limpa o input
            $('#cx')[0].scrollTop = $('#cx')[0].scrollHeight; // rola a barra pra baixo

            resposta(msg); // chama a função da resposta do bot e passa por parâmetro a msg (pergunta)

        }
        document.getElementById('txtArea').focus(); // joga o cursor para o input novamente se o usuário clicar no botão enviar
    }

    function resposta(pergunta) {
        getData(pergunta,"algodao")
        alert(JSON.stringify(top3))

        var divRobo = anim + "<div class='chat robo'><br><div class='foto'><img src='{{ url_for('static', filename = 'img/logo.png') }}'></div><br><div class='mensagem'>" + lista + "</div><br></div></div>" //concatena
        divChat.append(divRobo); //coloca dentro da caixa de msgs
        $('#cx')[0].scrollTop = $('#cx')[0].scrollHeight; //rola pra baixo

    }

     function getData(pergunta,livro){
        $.ajax({
            url: '/getData',
            async:false,
            data: {
                "pergunta" : pergunta, "livro" : livro
            },
            type: 'POST',
            success: function(data) {
                top3 = $.parseJSON(data);
                //alert(JSON.stringify(resposta["0"]));
                //alert(JSON.stringify(resposta));
            },
            error: function(error) {
                console.log("Error");
            }
        });
    }
