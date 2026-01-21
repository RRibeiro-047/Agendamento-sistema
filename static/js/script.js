$("#formAgendamento").submit(function(e){
    e.prevenDefault();

    $.ajax({
        url: "/agendar",
        method: "POST",
        contentType: "application/json",
        data: JSON.stringify({
            nome: $("#nome").val(),
            servico: $("#servico").val(),
            data: $("#data").val(),
            hora: $("#hora").val()
        }),
        success: function(){
            $("#mensagem").html("<div class='alert alert-success'>Agendamento Realizado!</div>");
            $("#formAgendamento")[0].reset();
        },
        error: function(){
            $("#mensagem").html("<div class='alert alert-danger'>Erro ao realizar agendamento!</div>");
        }
    });
})