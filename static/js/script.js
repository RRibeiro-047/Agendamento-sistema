$("#formAgendamento").submit(function(e){
    e.prevenDefault();

    $.ajax({
        url: "/agendar",
        method: "POST",
        cont
    })
})